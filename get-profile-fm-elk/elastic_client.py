from elasticsearch import Elasticsearch


"""Limit max hitable size to control performance"""
MAX_HIT_SIZE = 1000

class ElasticClient:
    """Client to deal with Elasticsearch

    Returns:
        dict: hits
    """
    def __init__(self, es_config: dict):
        self.es = Elasticsearch({
            'scheme': es_config['scheme'], 
            'host': es_config['host'], 
            'port': es_config['port']
            })
        self.index = es_config['index']
    
    def search_profiles(self, key_name: str, keys: list):
        query = {
            'query': {
                'terms': {
                    key_name: keys
                }
            }
        }
        response = self.es.search(
            index=self.index,
            body=query, 
            size= MAX_HIT_SIZE)
        
        return response['hits']['hits']
    