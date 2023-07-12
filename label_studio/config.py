from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv('.env')

@dataclass
class Config:
    label_studio_url = os.getenv('LABEL_STUDIO_URL')
    api_key = os.getenv('API_KEY')
    
    azure_connection_string = os.getenv('AZURE_CONNECTION_STRING')
    azure_account_name = os.getenv('AZURE_ACCOUNT_NAME')
    azure_container = os.getenv('AZURE_CONTAINER')
    
    