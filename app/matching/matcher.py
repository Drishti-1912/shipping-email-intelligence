def calculate_match_score(
    vessel,
    cargo
):

    score = 0

    vessel_port = (
        vessel.open_port or ""
    ).upper()

    load_port = (
        cargo.loading_port or ""
    ).upper()

    # --------------------
    # Port Matching
    # --------------------

    if vessel_port and load_port:

        if vessel_port == load_port:

            score += 40

        elif (
            len(vessel_port) >= 3
            and len(load_port) >= 3
            and vessel_port[:3] == load_port[:3]
        ):

            score += 20

    # --------------------
    # Vessel Information
    # --------------------

    if vessel.vessel_name:

        score += 10

    if vessel.vessel_size:

        score += 15

    # --------------------
    # Cargo Information
    # --------------------

    if cargo.cargo_name:

        score += 15

    if cargo.loading_port:

        score += 5

    if cargo.discharge_port:

        score += 10

    if cargo.laycan:

        score += 5

    return min(score, 100)


def find_matches(
    vessels,
    cargoes
):

    matches = []

    for vessel in vessels:

        for cargo in cargoes:

            score = calculate_match_score(
                vessel,
                cargo
            )

            matches.append({

                "vessel":
                    vessel.vessel_name,

                "vessel_size":
                    vessel.vessel_size,

                "open_port":
                    vessel.open_port,

                "open_date":
                    vessel.open_date,

                "cargo":
                    cargo.cargo_name,

                "loading_port":
                    cargo.loading_port,

                "discharge_port":
                    cargo.discharge_port,

                "laycan":
                    cargo.laycan,

                "score":
                    score
            })

    matches.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return matches


def get_top_opportunity(
    vessels,
    cargoes
):

    matches = find_matches(
        vessels,
        cargoes
    )

    if not matches:

        return None

    return matches[0]