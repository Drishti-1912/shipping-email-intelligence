from app.search.search import (
    get_vessels,
    get_vc_cargoes
)

from app.matching.matcher import (
    find_matches
)

matches = find_matches(
    get_vessels(),
    get_vc_cargoes()
)

for match in matches:

    print(match)
    
# Future Scope:
# Automatic matching of suitable vessels and cargoes