from minio import Minio
from minio.error import S3Error
import tempfile
import json
import logging
from typing import List, Dict

def try_except_minio(func):
    def function_try_except(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except S3Error as err:
            logging.error(err)
    return function_try_except

class MinIOClient:
    """
    A class representing a connection to a Minio server.
    Attributes:
        host (str): The hostname of the Minio server.
        port (int): The port number of the Minio server.
        access_key (str): The access key for authentication.
        secret_key (str): The secret key for authentication.
        temp_dir (tempfile.TemporaryDirectory): Temporary directory for file operations.
        minio_client (Minio): Minio client instance.
    """

    def __init__(self, host: str, port: int, access_key: str, secret_key: str):
        self.host = host 
        self.port = port 
        self.access_key = access_key
        self.secret_key = secret_key
        self.temp_dir = tempfile.TemporaryDirectory()
        self.minio_client = self.create_minio_client()

    def create_minio_client(self)-> Minio:
        """
        Creates a Minio client instance.

        Returns:
            Minio: The Minio client instance.
        """
        minio_client = Minio(
            f"{self.host}:{self.port}",
            access_key = self.access_key,
            secret_key = self.secret_key,
            secure=False
        )
        return minio_client
    
    @try_except_minio
    def insert_file(self, bucket_name: str, file_name: str, local_file_name: str):
        """
        Inserts a file into the specified bucket on the Minio server.
        Args:
            bucket_name (str): The name of the bucket.
            file_name (str): The name of the file in the bucket.
            local_file_name (str): The local path of the file to be uploaded.
        """
        self.minio_client.fput_object(
            bucket_name,
            file_name,  
            local_file_name  
        )
        logging.info("Upload realizado com sucesso!")

    @try_except_minio
    def list_bucket(self, bucket_name: str) -> List[str]:
        """
        Lists objects in the specified bucket on the Minio server.
        Args:
            bucket_name (str): The name of the bucket.
        Returs:
            List[str]: A list of object names in the bucket.
        """
        objects = self.minio_client.list_objects(bucket_name, recursive=True)
        ls_objects = []
        for obj in objects:
            ls_objects.append(obj.object_name)
        return ls_objects

    @try_except_minio
    def create_bucket(self, bucket_name: str):
        """
        Creates a new bucket on the Minio server.
        Args:
            bucket_name (str): The name of the bucket to be created.
        """
        self.minio_client.make_bucket(bucket_name)
        logging.info(f'bucket {bucket_name} criado com sucesso')


    def insert_string_to_minio(self, bucket_name: str,  dict_string: Dict, file_name: str):
        """
        Inserts a string (converted to JSON) into the specified bucket on the Minio server.
        Args:
            bucket_name (str): The name of the bucket.
            dict_string (Dict): A dictionary containing the string data.
            file_name (str): The name of the file to be created in the bucket.
        """
        message_file_temp_path = f"{self.temp_dir.name}/message.json"
        with open(message_file_temp_path, "w") as arquivo:
            json.dump(dict_string, arquivo)
        self.insert_file(bucket_name, file_name, message_file_temp_path)
        logging.info('string inserida como json com sucesso')

    def check_folder_in_bucket(self, bucket_name: str, folder_name: str) -> bool:
        """
        Checks if a folder exists in the specified bucket on the Minio server.
        Args:
            bucket_name (str): The name of the bucket.
            folder_name (str): The name of the folder to check.
        Returns:
            bool: True if the folder exists, False otherwise.
        """
        ls_objetos = list(self.list_bucket(bucket_name))
        cond = False
        for element in ls_objetos:
            if folder_name in element:
                cond = True 
        return cond