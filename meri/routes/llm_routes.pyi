from fastapi import FastAPI as FastAPI
from meri.domain.domain import Domain as Domain

def load_routes(fastapi_app: FastAPI, domain: Domain): ...
