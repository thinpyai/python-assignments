from src.elastic_client import ElasticClient
from config import Config

"""Limit max hitable size to control performance"""
MAX_HIT_SIZE = 1000


class ProfileService:
    """
    Service to process profiles.
    """

    def __init__(self, config: Config) -> None:
        """Initialize profile service configuration.

        Args:
            config (Config): Configuration.
        """
        elastic_config = config.get_elastic_config()
        self.es_client = ElasticClient(elastic_config)

    def search_profiles(self, key_name: str, keys: list) -> list:
        """Search profiles with multiple keys.

        Args:
            key_name (str): Key name to search
            keys (list): Keys to filter

        Returns:
            list: Profiles
        """
        profiles = []

        # Search by dividing into groups when key list is too big.
        for index in range(0, len(keys), MAX_HIT_SIZE):
            chunk = keys[index:index + MAX_HIT_SIZE]
            chunk_profiles = self.es_client.search_profiles(key_name, chunk)
            profiles.extend(chunk_profiles)

        return profiles
