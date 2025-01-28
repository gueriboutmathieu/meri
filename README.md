# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/meri/blob/python-coverage-comment-action-data/htmlcov/index.html)

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

[![Coverage badge](https://raw.githubusercontent.com/gueriboutmathieu/meri/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/meri/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gueriboutmathieu/meri/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/meri/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fgueriboutmathieu%2Fmeri%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/meri/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.