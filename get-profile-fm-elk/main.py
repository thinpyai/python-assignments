from config import Config
from profile_service import ProfileService
from file_helper import FileHelper


def main():

    # set the config
    config = Config()
    default_config = config.get_default_config()
    key_name = default_config.get('search_key_name', 'poi')

    # get search keys
    file_helper = FileHelper(config)
    keys = file_helper.read_from_file()

    # read data from elastic
    profile_service = ProfileService(config)
    raw_profiles = profile_service.search_profiles(key_name, keys)

    # output to file
    profiles = file_helper.filter_fields(raw_profiles)
    file_helper.write_to_file(profiles)


if __name__ == "__main__":
    main()
