from app.search.search import (
    get_vc_cargoes
)

cargoes = get_vc_cargoes()

for cargo in cargoes:

    print(cargo.cargo_name)