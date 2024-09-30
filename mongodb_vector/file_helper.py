import logging
from logging_config import setup_logging
import os
import pandas as pd
from pandas import DataFrame, Index


"""Setup logging"""
setup_logging()
logger = logging.getLogger(__name__)


class FileHelper:
    def __init__(self) -> None:
        pass

    def get_filename(self, file_path: str):
        return os.path.basename(file_path)

    def list_files(self, dir_path: str):
        return os.listdir(dir_path)

    def read_csv(self, file_path: str):
        return pd.read_csv(file_path)

    def get_csv_columns(self, df: DataFrame) -> Index:
        return df.columns

    def filter_columns(self, df_columns: Index, columns_to_drop: list):
        remaining_columns = df_columns.drop(columns_to_drop)
        return remaining_columns.tolist()

    def filter_csv_by_columns(self, df: DataFrame, columns: list):
        return df[columns]
