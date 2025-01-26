import uvicorn

from meri.config.openai_config import OpenaiConfig
from meri.domain.domain import Domain
from meri.services.llm import Llm
from meri.fastapi.fastapi_app import FastapiApp


openai_config = OpenaiConfig()
llm = Llm(api_key=openai_config.openai_api_key, model=openai_config.model)


class CommandContext:
    def __init__(self):
        self.llm = llm

    def commit(self):
        pass

    def rollback(self):
        pass



bound_domain = Domain(CommandContext)
fastapi_app = FastapiApp(bound_domain)


def run_server():
    uvicorn.run(fastapi_app.app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    run_server()
