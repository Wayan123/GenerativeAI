from dotenv import load_dotenv
import os
from constants import OPENAI_API_KEY_NAME


def get_openai_api_key() -> str:
    """
        Create OpenAI API Key from https://platform.openai.com/account/api-keys
    """
    load_dotenv()
    openai_api_key = os.environ.get(OPENAI_API_KEY_NAME, None)
    if not openai_api_key:
        raise ValueError("Please create .env file and store OpenAI API key with key as OPENAI_API_KEY")
    elif not openai_api_key.startswith('sk-'):
        raise ValueError("Invalid OpenAI API Key")

    return openai_api_key