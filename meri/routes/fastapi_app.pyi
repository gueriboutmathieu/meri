from _typeshed import Incomplete
from meri.domain.domain import Domain as Domain
from meri.routes import llm_routes as llm_routes

class FastapiApp:
    app: Incomplete
    def __init__(self, domain: Domain) -> None: ...
