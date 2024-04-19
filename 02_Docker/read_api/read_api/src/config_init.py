import os
from datetime import datetime 
from dotenv import load_dotenv

from classes.minio_client import MinIOClient

env = os.getenv('ENV', None) 

if not env:
    load_dotenv()
host = os.getenv('MINIO_HOST', None) 
port = os.getenv('MINIO_PORT', None)
access_key = os.getenv('MINIO_ROOT_USER', None)
secret_key = os.getenv('MINIO_ROOT_PASSWORD', None)

print(host, port, access_key, access_key, secret_key)

ls_buckets = ['taxes']

minio_connector = MinIOClient(host, port, access_key, secret_key)

print('Criando Buckets que serão utilizando no MINIO')
for bucket in ls_buckets:
    minio_connector.create_bucket(bucket)
