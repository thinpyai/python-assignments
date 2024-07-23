import json


class Config:
    """Service for reading Configuration from JSON file"""

    def __init__(self, file_path: str):
        """Initialize config file.

        Args:
            filename (str): Config file path
        """
        with open(file_path, 'r') as f:
            self.config = json.load(f)

    def get_default_config(self):
        """Get default configuration"""
        return self.config.get('default', {})

    def get_elastic_config(self):
        """Get elastic configuration"""
        return self.config.get('elastic', {})

    def get_input_config(self):
        """Get input file configuration"""
        return self.config.get('input', {})

    def get_output_config(self):
        """Get output file configuration"""
        return self.config.get('output', {})

    def get_sftp_config(self):
        """Get sftp server configuration"""
        return self.config.get('sftp', {})
