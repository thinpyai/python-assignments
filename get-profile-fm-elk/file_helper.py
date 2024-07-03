from config import Config
import csv


class FileHelper:

    def __init__(self, config: Config) -> None:
        output_config = config.get_output_config()
        self.target_fields = output_config.get(
            'fields', ['id', 'poi', 'profileType'])
        self.output_file_prefix = output_config.get('file_prefix', 'otc_profiles_')
        self.output_file_extension = output_config.get('file_extension', 'csv')

        input_config = config.get_input_config()
        self.input_file_name = input_config.get('file_name', 'input.txt')
        self.input_file_extension = input_config.get('file_extension', 'txt')

    def filter_fields(self, raw_profiles: list) -> list:
        """Filter the target fields of raw profiles

        Args:
            raw_profiles (list): Raw profiles which is searched from Elasticsearch
            target_fields (list, optional): Target fields. Defaults to [].

        Returns:
            list: _description_
        """
        profiles = []

        if not raw_profiles:
            # no data can be searched.
            return profiles

        for raw_profile in raw_profiles:
            source = raw_profile['_source']

            if not self.target_fields:
                print('Target fields to output are not set up.')
                # TODO to define exception
                raise Exception

            filtered_source = {
                field: source.get(field, '') for field in self.target_fields
            }
            profiles.append(filtered_source)

        return profiles

    def read_from_file(self):

        if not (self.input_file_name.lower() == 'txt'):
            print('Input file extension is not supported.')
            # TODO to define exception
            # raise exception

        file_path = self.input_file_name
        keys = []

        with open(file_path, mode='r') as file:
            keys = [line.strip() for line in file.readlines() if line.strip()]

        return keys

    def write_to_file(self, profiles: list):
        if not (self.output_file_extension.lower() == 'csv'):
            print('Output file extension is not supported.')
            # TODO to define exception
            # raise exception

        # TODO include ddmmyyyy to file name
        file_path = self.output_file_prefix + 'temp'

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.target_fields)
            writer.writeheader()
            writer.writerows(profiles)
