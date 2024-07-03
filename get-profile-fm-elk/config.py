import configparser


class Config:
    """Service for reading Configuration file

    Returns:
        _type_: _description_
    """

    def __init__(self):
        """ Initialize config file."""
        self.config = configparser.ConfigParser()
        # TODO pass config from arg
        self.config.read('config_sit.ini')

    def get_default_config(self):
        """Get default configuration
        """
        return self.config['default']
    
    def get_elastic_config(self):
        """Get elastic configuration
        """
        return self.config['elastic']

    def get_input_config(self):
        """Get input file configuration
        """
        return self.config['input']
        
    def get_output_config(self):
        """Get output file configuration
        """
        return self.config['output']
    