# Langchain Semantic Search

## Preqrequisites

- Python 3.10

- .env file

Create .env file in the root directory of the project and add the following variables

Get OpenAI API key from https://platform.openai.com/account/api-keys

```bash
OPENAI_API_KEY=<openai_api_key>
```

## Python Virtual Environment

Create a virtual environment for the project.

**NOTE**:
This project has a dependecy with `chromadb` Vector Store & this package is properly installed only with python 3.10.

When you try to install with 3.11, it will throw an error.

Hence, please make sure you have python 3.10 installed in your system & create a virtual environment with python 3.10

```bash
python3.10 -m venv {path_to_virtual_environment}
```

https://github.com/krishnamohanathota/PYTHON#python-virtual-environment

## Install Dependencies

```bash
pip install -r requirements.txt
```

To view all the installed packages

```bash
pip list

or

pip freeze
```

## Run

```bash
python main.py
```

## LangChain VectorstoreIndexCreator

https://python.langchain.com/docs/modules/data_connection/retrievers/#one-line-index-creation

- We are using LangChain `VectorstoreIndexCreator` to create a vectorstore index for the documents.
- Default VectorStore for this is `chromadb`
- Default Emebedding is `OpenAI embedding`

For more detailed and other ways to search, please refer to the [LangChain QnA NoteBook](https://github.com/krishnamohanathota/GenerativeAI/blob/main/langchain/langchain_llm_application_development/L4_DataConnection_QnA.ipynb)
