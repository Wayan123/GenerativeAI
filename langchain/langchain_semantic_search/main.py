from dotenv import load_dotenv
import openai
from api_key_utils import get_openai_api_key
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator

def load_data_create_index() -> VectorstoreIndexCreator:
    """
    Reading PDF and Creating Index:
    https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#using-pypdf

    """

    print("Loading the document.....")
    loader = PyPDFLoader("data/software-architecture-patterns.pdf")
    #pages = loader.load_and_split()
    #print(pages[0])
    # https://python.langchain.com/docs/modules/data_connection/retrievers/#one-line-index-creation
    print("Creating Index.....")
    index = VectorstoreIndexCreator().from_loaders([loader])
    print("Index is created.....")
    return index


if __name__ == "__main__":
    try:
        # Get OpenAI API Key
        openai.api_key = get_openai_api_key()
        vectorstoreindex = load_data_create_index()
        query = "Who is the author of this book?"
        print("#Prompt :" + query)
        print(vectorstoreindex.query(query))

        query = "Who had published this book and what was the exact published date?"
        print("#Prompt :" + query)
        print(vectorstoreindex.query(query))

        query = "What are different Architecture patterns discussed in this book?"
        print("#Prompt :" + query)
        print(vectorstoreindex.query(query))

        query = "Can you please provide a summary from the Event driven architecture?"
        print("#Prompt :" + query)
        print(vectorstoreindex.query(query))

    except ValueError as e:
        print(str(e)) 
        exit(1)   