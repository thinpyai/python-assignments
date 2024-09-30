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
    columns_to_drop = ['skip']
    columns_str = file_helper.filter_columns(columns,columns_to_drop)

    data = file_helper.filter_csv_by_columns(df, columns_str)

    # Developing

    selfie_image_path = 'selfie.jpeg'
    target_poi = '12/LaMaNa(N)123456'

    mongodb_client.match_selfie_cosine(selfie_image_path, target_poi)
    mongodb_client.search_selfie(selfie_image_path, target_poi)
    mongodb_client.vector_search_selfie(selfie_image_path, target_poi)

    print("===== Background Removed =====")

    # TODO remove sample data. get from input file
    selfie_image_path = 'selfie-removebg.jpg'
    target_poi = '9/LaMaNa(N)896546'

    mongodb_client.match_selfie_cosine(selfie_image_path, target_poi)
    mongodb_client.search_selfie(selfie_image_path, target_poi)
    mongodb_client.vector_search_selfie(selfie_image_path, target_poi)

    end_time = time.time()
    processing_time = end_time - start_time
    logger.info(f"Processing time is : {processing_time}")


if __name__ == '__main__':
    main()
