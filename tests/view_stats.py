from app.search.search import (
    get_vessels,
    get_vc_cargoes,
    get_tc_cargoes
)

print("VESSELS :", len(get_vessels()))
print("VC      :", len(get_vc_cargoes()))
print("TC      :", len(get_tc_cargoes()))