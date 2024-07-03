import configparser

class ConfigService:

    """ """
    
    def __init__(self, config_file_path: str):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)
    
    def get_settings(self):
        return self.config['DEFAULT']