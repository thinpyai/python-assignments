from config import Config
import csv
from datetime import datetime
import os
import paramiko
import logging
from src.logging_config import setup_logging

TXT_EXTENSION = '.txt'
FILE_NAME_TIME_FORMAT = "%d%m%Y_%H%M%S"

"""Setup logging"""
setup_logging()
logger = logging.getLogger(__name__)


class FileHelper:

    def __init__(self, config: Config) -> None:
        """Initialize file default configuration.

        Args:
            config (Config): Configuration setting
        """
        # Initial setup for config if the output file is in the same directory
        output_config = config.get_output_config()
        self.target_fields = output_config.get(
            'fields', 'id,poi,profileType').split(',')
        self.output_file_prefix = output_config.get(
            'file_prefix', 'otc_profiles_')
        self.output_file_extension = output_config.get(
            'file_extension', '.csv')

        # Initial setup for config if the input file is in the same directory
        input_config = config.get_input_config()
        self.input_file_name = input_config.get('file_name', 'input.txt')
        self.input_file_extension = input_config.get('file_extension', '.txt')
        self.complete_profile_only_flag = input_config.get(
            'complete_profile_only', 'true')

        # Initial setup for sftp config
        sftp_config = config.get_sftp_config()
        self.sftp_host = sftp_config.get('sftp_host', '')
        self.sftp_username = sftp_config.get('sftp_username', '')
        self.key_file_path = sftp_config.get('key_file_path', '')
        self.source_path = sftp_config.get(
            'source_path', '/otc-profile/input/input.txt')
        self.destination_dir = sftp_config.get(
            'destination_dir', '/otc-profile/output/')
        self.local_dir = sftp_config.get('local_dir', './')

    def filter_fields(self, raw_profiles: list) -> list:
        """Filter the target fields of raw profiles

        Args:
            raw_profiles (list): Raw profiles which is searched from Elasticsearch

        Raises:
            Exception: Target fields not exist.

        Returns:
            list: Profiles
        """
        profiles = []

        if not raw_profiles:
            # no data can be searched.
            return profiles

        for raw_profile in raw_profiles:
            source = raw_profile['_source']

            if not self.target_fields:
                logger.error(f'Target fields to output are not set up.')
                raise Exception('Target fields to output are not set up.')

            filtered_source = {
                field: source.get(field, '') for field in self.target_fields
            }
            profiles.append(filtered_source)

        return profiles

    def download_file_from_sftp(self) -> str:
        """Download target file (defined in config) from sftp file server.

        Raises:
            Exception: File download failure

        Returns:
            str: Downloaded file path in local
        """
        try:
            transport = paramiko.Transport((self.sftp_host, 22))
            private_key = paramiko.RSAKey.from_private_key_file(
                self.key_file_path)
            transport.connect(username=self.sftp_username, pkey=private_key)
            sftp = paramiko.SFTPClient.from_transport(transport)
            local_file_path = os.path.join(
                self.local_dir, os.path.basename(self.source_path))
            sftp.get(self.source_path, local_file_path)
            sftp.close()
            transport.close()
            logger.info(f"File downloaded from SFTP server: {
                        self.source_path}")
            return local_file_path

        except Exception as e:
            logger.error(f"Error downloading CSV file from SFTP server: {e}")
            raise Exception(
                f"Error downloading CSV file from SFTP server: {e}")

    def upload_file(self, local_file_path: str):
        """Upload file to sftp file server. 

        Args:
            local_file_path (str): File path in local

        Raises:
            Exception: File upload failure
        """
        try:
            transport = paramiko.Transport((self.sftp_host, 22))
            private_key = paramiko.RSAKey.from_private_key_file(
                self.key_file_path)
            transport.connect(username=self.sftp_username, pkey=private_key)
            sftp = paramiko.SFTPClient.from_transport(transport)
            file_name = os.path.basename(local_file_path)
            destination_path = self.destination_dir + file_name
            sftp.put(local_file_path, destination_path)
            sftp.close()
            transport.close()
            logger.info(f"Uploaded {local_file_path} to {destination_path}")

            # Delete local file after uploading
            self._delete_file(local_file_path)

        except Exception as e:
            logger.error(f"Error in uploading file: {e}")
            raise Exception(f"Error in uploading file: {e}")

    def read_from_file(self, local_file_path: str) -> list:
        """Read file from the file path in local.

        Args:
            local_file_path (str): File path in local

        Raises:
            Exception: Unsupported input file extension
            FileNotFoundError: File is not found
            PermissionError: Permission is not set
            Exception: Unexpected error in reading file

        Returns:
            list: Key list
        """
        _, input_file_extension = os.path.splitext(local_file_path)

        if not (input_file_extension == TXT_EXTENSION):
            logger.error('Input file extension is not supported.')
            raise Exception('Input file extension is not supported.')

        keys = []

        try:

            # Read lines from the file, strip whitespace and filter out empty lines
            with open(local_file_path, mode='r') as file:
                keys = [line.strip()
                        for line in file.readlines() if line.strip()]

            # Remove duplicate keys
            unique_keys = list(dict.fromkeys(keys))

            # Delete local file after reading
            self._delete_file(local_file_path)

            # Rename sftp file after reading to avoid duplicate reading
            new_file_path = self._create_new_filename(self.source_path)
            self._move_file_in_sftp(self.source_path, new_file_path)

        except FileNotFoundError:
            logger.error(f'The file {local_file_path} does not exist.')
            raise FileNotFoundError(
                f'The file {local_file_path} does not exist.')

        except PermissionError as e:
            logger.error(f'Do not have permission to access {
                         local_file_path}.')
            raise PermissionError(
                f'Do not have permission to access {local_file_path}.')

        except Exception as e:
            logger.error(f'Unexpected error occurs: {e}.')
            raise Exception(f'Unexpected error occurs: {e}.')

        return unique_keys

    def write_to_file(self, profiles: list) -> str:
        """Write to file in local.

        Args:
            profiles (list): Profiles

        Raises:
            Exception: Unsupported file extension.
            FileNotFoundError: File is not found.
            PermissionError: Permission is not set.
            Exception: Unexpected error in writing file.

        Returns:
            str: File path
        """
        if not (self.output_file_extension.lower() == '.csv'):
            logger.error('Output file extension is not supported.')
            raise Exception('Output file extension is not supported.')

        # include ddmmyyyy_hhmmss to file name
        now = datetime.now()
        date_str = now.strftime(FILE_NAME_TIME_FORMAT)

        file_path = self.output_file_prefix + \
            date_str + self.output_file_extension.lower()

        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.target_fields)
                writer.writeheader()
                for profile in profiles:
                    if profile.get('profileType') == 'OTC':
                        writer.writerow(profile)
        except FileNotFoundError:
            logger.error(f'The file {file_path} does not exist.')
            raise FileNotFoundError(f'The file {file_path} does not exist.')

        except PermissionError:
            logger.error(f'Do not have permission to access {file_path}.')
            raise PermissionError(
                f'Do not have permission to access {file_path}.')

        except Exception as ex:
            logger.error(f'Unexpected error occurs: {ex}.')
            raise Exception(f'Unexpected error occurs: {ex}.')

        return file_path

    def _move_file_in_sftp(self, source_path: str, destination_path: str):
        """Move file in sftp file server from source to destination.

        Args:
            source_path (str): Source file path
            destination_path (str): Destination file path

        Raises:
            FileNotFoundError: File not found.
            Exception: Unexpected error in file moving.
        """
        try:
            transport = paramiko.Transport((self.sftp_host, 22))
            private_key = paramiko.RSAKey.from_private_key_file(
                self.key_file_path)
            transport.connect(username=self.sftp_username, pkey=private_key)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.rename(source_path, destination_path)
            sftp.close()
            transport.close()
            logger.info(f"Moved file from {source_path} to {destination_path}")
        except FileNotFoundError:
            logger.error(f"Source file not found at {source_path}")
            raise Exception(f"Source file not found at {source_path}")
        except Exception as e:
            logger.error(f"Error moving file: {e}")
            raise Exception(f"Error moving file: {e}")

    def _create_new_filename(self, file_name: str) -> str:
        """Create new filename based on the existing file name.

        Args:
            file_name (str): File name

        Returns:
            str: New filename
        """
        now = datetime.now()
        date_str = now.strftime(FILE_NAME_TIME_FORMAT)
        old_filename, ext = os.path.splitext(file_name)
        new_filename = f'{old_filename}_processed_{date_str}{ext}'
        return new_filename

    def _delete_file(self, local_file_path: str):
        """Delete the file in local.

        Args:
            local_file_path (str): File path in local

        Raises:
            Exception: Unexpected error in deleting file.
        """
        try:
            os.remove(local_file_path)
            logger.info(f'Delete {local_file_path} after reading keys.')
        except Exception as e:
            logger.error(f'Unexpected error occurs in deleting file: {e}.')
            raise Exception(f'Delete {local_file_path} after reading keys.')
