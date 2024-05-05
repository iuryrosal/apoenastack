from datetime import datetime
import time
import logging
import os
from src.classes.minio_client import MinIOClient


class IngestionProcess:
    def __init__(self) -> None:
        host = os.getenv('MINIO_HOST', None) 
        port = os.getenv('MINIO_PORT', None)
        access_key = os.getenv('MINIO_ROOT_USER', None)
        secret_key = os.getenv('MINIO_ROOT_PASSWORD', None)

        self.minio_connector = MinIOClient(host, port, access_key, secret_key) 

    def generate_sink_file_name(self, namespace, zone):
        now = datetime.now()
        timestamp = int(time.time())
        file_name = f"{now.year}_{now.month}_{now.day}_{str(timestamp)}"
        return f"{namespace}/{zone}/{file_name}.json"
    
    def store_file(self, data, namespace, zone):
        sink_path = f"{self.generate_sink_file_name(namespace, zone)}"
        self.minio_connector.insert_string_to_minio(namespace, data, sink_path)
        print(f'File {sink_path} inserted in {namespace}!')