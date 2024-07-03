from elastic_client import ElasticClient
from config import Config


class ProfileService:

    def __init__(self, config: Config) -> None:
        elastic_config = config.get_elastic_config()
        self.es_client = ElasticClient(elastic_config)

    def search_profiles(self, key_name: str, keys: list):
        profiles = self.es_client.search_profiles(key_name, keys)
        return profiles

        # 
        # return profiles


