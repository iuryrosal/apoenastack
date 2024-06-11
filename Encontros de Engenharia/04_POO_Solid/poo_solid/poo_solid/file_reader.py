from abc import ABC, abstractmethod
import pandas as pd


class FileReader(ABC):
    @abstractmethod
    def read_file(self, path: str) -> pd.DataFrame:
        pass


class CsvReader(FileReader):
    def read_file(self, path: str, dtype_dict: dict, parse_dates: list, column_names: list = []) -> pd.DataFrame:
        if len(column_names) == 0:
            return pd.read_csv(
                filepath_or_buffer=path,
                sep=",",
                dtype=dtype_dict,
                parse_dates=parse_dates
            )
        else:
            return pd.read_csv(
                filepath_or_buffer=path,
                sep=",",
                names=column_names,
                dtype=dtype_dict,
                parse_dates=parse_dates
            )


class TxtReader(FileReader):
    def read_file(self, path: str, dtype_dict: dict, parse_dates: list, column_names: list) -> pd.DataFrame:
        return pd.read_csv(
            filepath_or_buffer=path,
            sep="\t",
            header=0,
            names=column_names,
            dtype=dtype_dict,
            parse_dates=parse_dates
        )
