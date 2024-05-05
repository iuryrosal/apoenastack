from dotenv import load_dotenv
import os

from src.classes.brasil_api import BrasilAPI
from src.classes.ingest_process import IngestionProcess

env = os.getenv('ENV', None) 
if not env:
    load_dotenv()

print('Collect data from API...')

brasil_api = BrasilAPI()
taxes_data = brasil_api.get_taxes()

print(taxes_data)

print('Send the data to MinIO...')

ingestion_process = IngestionProcess()
ingestion_process.store_file(namespace="taxes", zone="raw", data=taxes_data)

print('Ingestion Complete...')