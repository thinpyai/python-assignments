from elasticsearch import Elasticsearch
import logging
from src.logging_config import setup_logging

"""Limit max hitable size to control performance"""
MAX_HIT_SIZE = 1000

"""Setup logging"""
setup_logging()
logger = logging.getLogger(__name__)


class ElasticClient:
    """Client to deal with Elasticsearch

    Returns:
        dict: hits
    """

    def __init__(self, es_config: dict):
        """Initialize Elasticsearch client

        Args:
            es_config (dict): Elasticsearch config
        """
        self.es = Elasticsearch(f'{es_config['scheme']}://{es_config['host']}:{
                                es_config['port']}', basic_auth=(es_config['username'], es_config['password']))
        self.index = es_config['index']
        self.complete_profile_only_flag = es_config.get(
            'complete_profile_only', 'true')

    def search_profiles(self, key_name: str, keys: list) -> list:
        """Search profiles from Elasticsearch

        Args:
            key_name (str): Key name to search
            keys (list): Keys

        Raises:
            Exception: No keys to search
            Exception: Unexpected error in searching

        Returns:
            list: Hit results
        """

        if not keys:
            # No keys to search
            logger.error(f'No keys to search. keys : {keys}')
            raise Exception(f'No keys to search. keys : {keys}')

        query = {
            'query': {
                'bool': {
                    'filter': [
                        {
                            'terms': {
                                key_name: keys
                            }
                        }
                    ]
                }
            }
        }

        if self.complete_profile_only_flag != 'true':
            otc_profile_filter = {
                'term': {
                    'profileType': 'OTC'
                }
            }
            query['query']['bool']['filter'].append(otc_profile_filter)

        try:
            response = self.es.search(
                index=self.index,
                body=query,
                size=MAX_HIT_SIZE)

            logger.info(f'Searching success. hit counts : {
                        len(response['hits']['hits'])}')

        except Exception as e:
            logger.error(f'Unexpected error occurs in searching data. index: {
                         self.index}, query: {query}, max_hit_size: {MAX_HIT_SIZE}, exception: {e}.')
            raise Exception(f'Unexpected error occurs in searching data. index: {
                            self.index}, query: {query}, max_hit_size: {MAX_HIT_SIZE}, exception: {e}.')

        return response['hits']['hits']
