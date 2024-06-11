from etl_processor import ETLBatchTable
from file_reader import CsvReader, TxtReader
import numpy as np

csv_reader = CsvReader()

txt_reader = TxtReader()

etl_batch_table = ETLBatchTable(obj_file_reader=csv_reader)

etl_batch_table.extract_data(path="files/exchange_rates.csv",
                             dtype_dict={
                                "Country/Currency": str,
                                "currency": str,
                                "value": np.float64
                             },
                             parse_dates=["date"])

print(etl_batch_table.dataframe_extracted.head(5))

etl_batch_table_txt = ETLBatchTable(obj_file_reader=txt_reader)

etl_batch_table_txt.extract_data(path="files/SampleCurrencyData.txt",
                                 dtype_dict={
                                       "AverageRate": np.float64,
                                       "CurrencyID": str,
                                       "EndOfDayRate": np.float64
                                 },
                                 parse_dates=["CurrencyDate"],
                                 column_names=["AverageRate", "CurrencyID", "CurrencyDate", "EndOfDayRate"])

print(etl_batch_table_txt.dataframe_extracted.head(5))