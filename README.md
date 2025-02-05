# Meri

Your loyal companion, helping you stay organized and remember what truly matters.

Meri Server is a python backend which exposes only 1 endpoint `/query`.
It takes a string as input, categorize it as `statement` or `question`.
If this is a statement like `I need to buy some eggs at the store today.`, this sentence will be embed and stored in the database.
If this is a question like `What do I need to buy to the store today ?`, this sentence will be embed and the database will find nearest statements that best match the question.
Finally, a Llm will generate an appropriate response based on the question and nearest statements found.
Technically, this is the level 1 of a RAG (Retrieval-augmented generation) project.

To use Meri, check the frontend apps:
- [web app](https://github.com/gueriboutmathieu/meri_web.git)

## Install locally

First, you need [uv](https://github.com/astral-sh/uv) to be installed.

If you are on NixOs, you need a FHS compliant environment, so run this command each time you need to use uv.
(Zlib is needed for some python packages that does not work very well with nix dynamic binaries)
```shell
nix-shell -E 'with import <nixpkgs> {}; (pkgs.buildFHSUserEnv { name = "fhs"; targetPkgs = pkgs: ([ pkgs.zlib ]); runScript = "zsh"; }).env'
```
note: replace `zsh` by the shell you use. (It helps you to keep your shell env with aliases and config inside fhs)

This project uses python 3.11.
```shell
uv python install 3.11
```

Then, setup venv and activate it :
```shell
uv venv
source .venv/bin/activate
```

Finally, install dependencies :
```shell
uv sync
```

## Environment variables
Create a `.env` file with these variables:
```
SQL_USER=user
SQL_PASSWORD=password
SQL_HOST=localhost
SQL_PORT=55432
SQL_DATABASE=meri
OPENAI_API_KEY=<your-openai-api-key>
OPENAI_LLM_MODEL=<openai-llm-model>
OPENAI_EMBEDDING_MODEL=<openai-embedding-model>
VECTOR_DIMENSIONS=1536
VECTOR_DATABASE_FILE_PATH=vector_database.bin
```

## Run locally
Run postgresql database:
```shell
docker compose up -d
```

In order to run migrations, you may need to export your env vars:
```shell
set -a
source .env
set +a
```

Run migrations:
```shell
alembic upgrade head
```

Run the app:
```shell
python meri/app.py
```

## Run the tests
```shell
pytest tests
```

## Run Coverage
```shell
coverage run -m pytest tests
coverage report -m
```

## Contribute
This will install pre-commit hook to run multiple checks, ruff and pyright before committing.
```shell
pre-commit install
```

## License
This project is licensed under the GNU General Public License v3.0 (GPL v3).
You are free to use, modify, and distribute this software, as long as any distributed version is also licensed under GPLv3.
This software is provided "as is", without warranty of any kind.
See the [LICENSE](LICENSE) file for more details.
