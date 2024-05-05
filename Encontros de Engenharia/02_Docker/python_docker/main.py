from dotenv import load_dotenv
import os

from src.brasil_api import BrasilAPI

env = os.getenv('ENV', None) 
if not env:
    load_dotenv()

print('Collect data from API...')

brasil_api = BrasilAPI()
taxes_data = brasil_api.get_taxes()

print(taxes_data)
