import logging
from logging_config import setup_logging

"""Setup logging"""
setup_logging()
logger = logging.getLogger(__name__)

def insert_dummy_to_db(file_helper, mongodb_client):
    mongodb_client.create_collection()
    mongodb_client.create_search_index()

    # Insert dummy data
    insert_dummy_data(file_helper, mongodb_client)

def insert_dummy_data(file_helper, mongodb_client):
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
