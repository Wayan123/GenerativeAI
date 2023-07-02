## LangChain Chat with database

Integrate LangChain with database.

https://python.langchain.com/docs/modules/chains/popular/sqlite

## Virtaul Environment Setup

https://github.com/krishnamohanathota/PYTHON#python-virtual-environment

Create a virtual environment

    python3 -m venv /path/to/new/virtual/environment

To activate the virtual environment

    - cd /path/to/new/virtual/environment
    - source bin/activate

To deactivate the virtual environment

    deactivate

To view list of installed packages

    python3 -m pip list

    Package    Version
    ---------- -------
    pip        23.1.2
    setuptools 58.1.0

## Install Dependencies

Install `langchain`,`openai`, `python-environ` and `psycopg2` libraries using pip.

    pip install langchain openai python-environ
    pip install psycopg2 or pip install psycopg2-binary

    Note : If you face any issues with `psycopg2` installation, please refer to the below link & install `psycopg2-binary'

    https://stackoverflow.com/questions/74727501/error-could-not-build-wheels-for-psycopg2-which-is-required-to-install-pyproje

## Install PostgreSQL

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

## Create .env file

Create a `.env` file in the root directory of the project and add the below environment variables.

```
OPENAI_API_KEY=<open api key>
DBPASS=<postgres db username>
DATABASE=<postgres db name>
```

## Load data

    python3 load_data.py

## Run

    python3 chat_with_database.py
