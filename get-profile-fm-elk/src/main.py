from config import Config
from src.profile_service import ProfileService
from src.file_helper import FileHelper
import argparse


def main():
    """
    Main process
    """
    # get config file_path
    parser = argparse.ArgumentParser(
        description='Get complete OTC user profiles job')
    parser.add_argument('file_path', type=str, help='Configuration file path')
    args = parser.parse_args()
    file_path = args.file_path

    # set the config
    config = Config(file_path)
    default_config = config.get_default_config()
    key_name = default_config.get('search_key_name', 'poi')

    # get search keys
    file_helper = FileHelper(config)
    local_file_path = file_helper.download_file_from_sftp()
    keys = file_helper.read_from_file(local_file_path)

    # read data from elastic
    profile_service = ProfileService(config)
    raw_profiles = profile_service.search_profiles(key_name, keys)

    # output to file and upload to sftp
    profiles = file_helper.filter_fields(raw_profiles)
    local_file_path = file_helper.write_to_file(profiles)
    file_helper.upload_file(local_file_path)


if __name__ == "__main__":
    main()
