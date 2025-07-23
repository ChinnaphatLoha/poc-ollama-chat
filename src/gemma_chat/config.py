import os
from dotenv import load_dotenv


def load_config():
    load_dotenv()
    return {
        'model': os.getenv('GEMMA_MODEL', 'gemma:2b'),
    }
