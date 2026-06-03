import streamlit as st
import pandas as pd

from app.search.search import (
    get_vessels,
    get_vc_cargoes,
    get_tc_cargoes
)
from app.pipeline.email_processor import (
    process_email
)
from app.matching.matcher import (
    find_matches
)

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="Shipping Email Intelligence",
    layout="wide"
)

# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose Page",
    [
        "Dashboard",
        "Matching Engine",
        "Process Email",
        "Market Opportunities",
        "Review Queue"
    ]
)

# -------------------------
# LOAD DATA
# -------------------------

vessels = get_vessels()
vc_cargoes = get_vc_cargoes()
tc_cargoes = get_tc_cargoes()

# =====================================================
# DASHBOARD PAGE
# =====================================================

if page == "Dashboard":

    st.title("🚢 Shipping Email Intelligence Dashboard")

    st.header("📊 Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Vessels",
            len(vessels)
        )

    with col2:
        st.metric(
            "VC Cargoes",
            len(vc_cargoes)
        )

    with col3:
        st.metric(
            "TC Cargoes",
            len(tc_cargoes)
        )

    st.divider()

    # -------------------------
    # VESSELS
    # -------------------------

    st.header("🚢 Open Vessels")

    vessel_data = []

    for vessel in vessels:

        vessel_data.append({

            "Vessel Name":
                vessel.vessel_name,

            "Open Port":
                vessel.open_port,

            "Open Date":
                vessel.open_date,

            "Vessel Size":
                vessel.vessel_size
        })

    if vessel_data:

        st.dataframe(
            pd.DataFrame(vessel_data),
            use_container_width=True
        )

    else:

        st.info(
            "No vessel data found."
        )

    st.divider()

    # -------------------------
    # VC CARGOES
    # -------------------------

    st.header("📦 Voyage Charter Cargoes")

    vc_data = []

    for cargo in vc_cargoes:

        vc_data.append({

            "Cargo":
                cargo.cargo_name,

            "Loading Port":
                cargo.loading_port,

            "Discharge Port":
                cargo.discharge_port,

            "Laycan":
                cargo.laycan,

            "Cargo Type":
                cargo.cargo_type
        })

    if vc_data:

        st.dataframe(
            pd.DataFrame(vc_data),
            use_container_width=True
        )

    else:

        st.info(
            "No VC cargoes found."
        )

    st.divider()

    # -------------------------
    # TC CARGOES
    # -------------------------

    st.header("⏳ Time Charter Cargoes")

    tc_data = []

    for cargo in tc_cargoes:

        tc_data.append({

            "Account":
                cargo.account_name,

            "Delivery Port":
                cargo.delivery_port,

            "Redelivery Port":
                cargo.redelivery_port,

            "Duration":
                cargo.duration,

            "Laycan":
                cargo.laycan
        })

    if tc_data:

        st.dataframe(
            pd.DataFrame(tc_data),
            use_container_width=True
        )

    else:

        st.info(
            "No TC cargoes found."
        )

# =====================================================
# MATCHING ENGINE PAGE
# =====================================================

elif page == "Matching Engine":

    st.title("🎯 Vessel-Cargo Matching")

    matches = find_matches(
        vessels,
        vc_cargoes
    )

    st.write("Vessels:", len(vessels))
    st.write("VC Cargoes:", len(vc_cargoes))
    st.write("Matches:", len(matches))

    match_data = []

    for match in matches:

        match_data.append({

            "Vessel":
                match["vessel"],

            "Open Port":
                match["open_port"],

            "Cargo":
                match["cargo"],

            "Loading Port":
                match["loading_port"],

            "Discharge Port":
                match["discharge_port"],

            "Score":
                match["score"]
        })

    if match_data:

        st.dataframe(
            pd.DataFrame(match_data),
            width="stretch"
        )

    else:

        st.warning("No matches found.")
        
#------------------------------------------Process Email Page-----------------------------------------------------------------
            
elif page == "Process Email":

    st.title("📧 Process Shipping Email")

    uploaded_file = st.file_uploader(
        "Upload Email File",
        type=["txt"]
    )

    email_text = ""

    if uploaded_file is not None:

        email_text = uploaded_file.read().decode("utf-8")

        st.text_area(
            "Email Content",
            email_text,
            height=300
        )

    else:

        email_text = st.text_area(
            "Paste Shipping Email Here",
            height=300
        )

    if st.button("Process Email"):

        result = process_email(
            email_text
        )

        if result["saved"]:

            st.success(
                "New record saved successfully!"
            )

        else:

            st.warning(
                "Duplicate email detected or no new records added."
            )
            
            st.metric(
                "Confidence",
                f"{result.get('confidence', 0)}%"
            )

        st.json(result)
        
# -----------------------MARKET OPPORTUNITIES PAGE -----------------------
        
elif page == "Market Opportunities":

    st.title("💰 Market Opportunities")

    matches = find_matches(
        vessels,
        vc_cargoes
    )

    if not matches:

        st.warning(
            "No opportunities found."
        )

    else:

        best_match = matches[0]

        st.subheader(
            "🏆 Top Market Opportunity"
        )

        st.success(
            f"""
Vessel: {best_match['vessel']}

Open Port: {best_match['open_port']}

Cargo: {best_match['cargo']}

Route:
{best_match['loading_port']} → {best_match['discharge_port']}

Opportunity Score: {best_match['score']}%
"""
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Vessels",
                len(vessels)
            )

        with col2:
            st.metric(
                "Total Cargoes",
                len(vc_cargoes)
            )

        with col3:
            st.metric(
                "Best Score",
                f"{best_match['score']}%"
            )

        st.divider()

        st.subheader(
            "All Opportunities"
        )

        opportunity_data = []

        for match in matches:

            opportunity_data.append({

                "Vessel":
                    match["vessel"],

                "Size":
                    match["vessel_size"],

                "Cargo":
                    match["cargo"],

                "Route":
                    f"{match['loading_port']} → {match['discharge_port']}",

                "Laycan":
                    match["laycan"],

                "Score":
                    f"{match['score']}%"
            })

        st.dataframe(
            pd.DataFrame(opportunity_data),
            width="stretch"
        )
              
              
#-----------------------Review Page ----------------------------------------
elif page == "Review Queue":

    st.title("🔍 Review Queue")

    st.info(
        "Records with confidence below 70%"
    )

    st.write(
        "Review Queue functionality coming next."
    )  

# streamlit run dashboard.py