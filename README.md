# Repository Coverage



| Name                                            |    Stmts |     Miss |   Cover |   Missing |
|------------------------------------------------ | -------: | -------: | ------: | --------: |
| meri/\_\_init\_\_.py                            |        0 |        0 |    100% |           |
| meri/app.py                                     |       36 |       36 |      0% |      1-74 |
| meri/config/\_\_init\_\_.py                     |        0 |        0 |    100% |           |
| meri/config/openai\_config.py                   |        6 |        0 |    100% |           |
| meri/config/postgresql\_config.py               |        8 |        0 |    100% |           |
| meri/config/vector\_config.py                   |        6 |        0 |    100% |           |
| meri/domain/\_\_init\_\_.py                     |        0 |        0 |    100% |           |
| meri/domain/command\_context.py                 |       29 |       15 |     48% |11, 15, 19, 22, 25, 33-45 |
| meri/domain/commands/\_\_init\_\_.py            |        0 |        0 |    100% |           |
| meri/domain/commands/query\_llm\_command.py     |       19 |        0 |    100% |           |
| meri/domain/domain.py                           |        7 |        0 |    100% |           |
| meri/domain/entities/\_\_init\_\_.py            |        0 |        0 |    100% |           |
| meri/domain/entities/prompt\_category\_enum.py  |        4 |        0 |    100% |           |
| meri/domain/entities/statement\_entity.py       |       13 |        0 |    100% |           |
| meri/domain/exceptions/\_\_init\_\_.py          |        0 |        0 |    100% |           |
| meri/domain/exceptions/statement\_exceptions.py |        6 |        2 |     67% |      3, 8 |
| meri/fastapi/\_\_init\_\_.py                    |        0 |        0 |    100% |           |
| meri/fastapi/fastapi\_app.py                    |       14 |        0 |    100% |           |
| meri/fastapi/routes/\_\_init\_\_.py             |        0 |        0 |    100% |           |
| meri/fastapi/routes/llm\_routes.py              |        6 |        0 |    100% |           |
| meri/repositories/\_\_init\_\_.py               |        0 |        0 |    100% |           |
| meri/repositories/statement\_repository.py      |       16 |        1 |     94% |        12 |
| meri/services/\_\_init\_\_.py                   |        0 |        0 |    100% |           |
| meri/services/embedding\_service.py             |       10 |        0 |    100% |           |
| meri/services/llm\_service.py                   |       18 |        0 |    100% |           |
|                                       **TOTAL** |  **198** |   **54** | **73%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://github.com/gueriboutmathieu/meri/raw/python-coverage-comment-action-data/badge.svg)](https://github.com/gueriboutmathieu/meri/tree/python-coverage-comment-action-data)

This is the one to use if your repository is private or if you don't want to customize anything.



## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.