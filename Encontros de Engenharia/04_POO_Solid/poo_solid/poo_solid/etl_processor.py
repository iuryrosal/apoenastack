from abc import ABC, abstractmethod
from file_reader import FileReader
import pandas as pd
import duckdb


class ETLProcessor(ABC):
    @abstractmethod
    def extract_data(self, path: str, dtype_dict: dict, parse_dates: list) -> pd.DataFrame:
        pass

    @abstractmethod
    def transform_data(self, columns_rename_dict: dict):
        pass

    @abstractmethod
    def load_data(self, path_db: str, table_name: str):
        pass


class ETLBatchTable(ETLProcessor):
    def __init__(self, obj_file_reader: FileReader) -> None:
        super().__init__()
        self.dataframe_extracted = None
        self.file_reader = obj_file_reader

    def extract_data(self, path: str, dtype_dict: dict, parse_dates: list, column_names: list = []) -> pd.DataFrame:
        self.dataframe_extracted = self.file_reader.read_file(path=path,
                                                              column_names=column_names,
                                                              dtype_dict=dtype_dict,
                                                              parse_dates=parse_dates)

    def transform_data(self, columns_rename_dict: dict):
        self.dataframe_extracted.rename(
            columns=columns_rename_dict,
            inplace=True
        )

    def load_data(self, path_db: str, table_name: str):
        duck_con = duckdb.connect(database=path_db)
        duck_con.sql(f"""CREATE TABLE IF NOT EXISTS {table_name}
                        AS SELECT *
                        FROM self.dataframe_extracted""")