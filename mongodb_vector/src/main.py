import os

from file_helper import FileHelper
from logging_config import setup_logging
import logging
import time
from mongodb_client import MongoDBClient
from dummy import insert_dummy_to_db

"""Setup logging"""
setup_logging()
logger = logging.getLogger(__name__)


def main():
    start_time = time.time()

    mongodb_client = MongoDBClient()
    file_helper = FileHelper()

    # TODO Get from setting
    is_initial = False

    if is_initial:
        # Insert dummy data
        insert_dummy_to_db(file_helper, mongodb_client)

    # TODO get input.csv file path from run argument
    input_csv_file_path = 'input.csv'
    df = file_helper.read_csv(input_csv_file_path)
    columns = file_helper.get_csv_columns(df)

    # TODO Get columns from setting
    columns_to_drop = ['note']
    columns_str = file_helper.filter_columns(columns,columns_to_drop)

    subset = file_helper.filter_csv_by_columns(df, columns_str)

    target_poi = ''
    selfie_image_path = ''
    selfie_nobg_image_path = ''
    for index, row in subset.iterrows():
        for col_name in subset.columns:
            if col_name == 'poi':
                target_poi = row[col_name]
            elif col_name == 'img':
                selfie_image_path = row[col_name]
            elif col_name == 'no_bg_img':
                selfie_nobg_image_path = row[col_name]

            if target_poi and selfie_image_path:
                print("===== With Background =====")
                mongodb_client.match_selfie_cosine(selfie_image_path, target_poi)
                mongodb_client.search_selfie(selfie_image_path, target_poi)
                mongodb_client.vector_search_selfie(selfie_image_path, target_poi)

            elif target_poi and selfie_nobg_image_path:
                print("===== Without background =====")
                mongodb_client.match_selfie_cosine(selfie_nobg_image_path, target_poi)
                mongodb_client.search_selfie(selfie_nobg_image_path, target_poi)
                mongodb_client.vector_search_selfie(selfie_nobg_image_path, target_poi)



    end_time = time.time()
    processing_time = end_time - start_time
    logger.info(f"Processing time is : {processing_time}")


if __name__ == '__main__':
    main()
