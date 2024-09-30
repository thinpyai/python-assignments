import os

from file_helper import FileHelper
from logging_config import setup_logging
import logging
import time
from mongodb_client import MongoDBClient

"""Setup logging"""
setup_logging()
logger = logging.getLogger(__name__)


def main():
    start_time = time.time()

    mongodb_client = MongoDBClient()
    file_helper = FileHelper()

    is_initial = False

    if is_initial:
        insert_data_to_db(file_helper, mongodb_client)

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


def insert_data_to_db(file_helper, mongodb_client):
    mongodb_client.create_collection()
    mongodb_client.create_search_index()
    insert_sample_data(file_helper, mongodb_client)


def insert_sample_data(file_helper, mongodb_client):
    dir_path = './images/'
    poi_list = [
        '12/LaMaNa(N)9876543',
        '1/PaBaMa(C)345678',
        '12/LaMaNa(N)123456',
        '3/LaMaNa(N)456234',
        '5/LaMaNa(N)3400984'
        '12/LaMaNa(N)9876543',
        '6/LaMaNa(N)231212',
        '7/LaMaNa(N)343434',
        '8/LaMaNa(N)565678',
        '9/LaMaNa(N)896546'
    ]
    file_path_list = file_helper.list_files(dir_path)
    for index in range(len(file_path_list)):
        img_file_name = file_path_list[index]
        allowed_extensions = ('.png', '.jpg', '.jpeg')
        if not img_file_name.lower().endswith(allowed_extensions):
            continue
        poi = poi_list[index]
        local_img_path = f'{dir_path}{img_file_name}'
        mongodb_client.save_image_and_embedding(local_img_path, poi)
    logger.info(f"Inserted sample data to DB.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
