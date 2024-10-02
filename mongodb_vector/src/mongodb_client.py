import gridfs
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from pymongo.collection import  Collection
from embedding_util import generate_embedding, compare_img_by_cosine, compare_by_mongo_search, calculate_mongodb_vectore_score,compare_by_mongo_vector_search
from pymongo.server_api import ServerApi

from logging_config import setup_logging
import logging
import ssl

from file_helper import FileHelper

"""Setup logging"""
setup_logging()
logger = logging.getLogger(__name__)

PROTOCOL = 'mongodb+srv'
CLUSTER = 'tp-learning-cluster.bil2g.mongodb.net'
DB_USER_NAME = 'thinpyaiwin'
DB_PASSPORT = 'zHNMtTu54da0tIlB'
DB_NAME = 'user_info'
SELFIE_COLLECTION_NAME = 'selfie'
INDEX_NAME = 'default'
POI_INDEX_NAME = 'poi'
SELFIE_INDEX_NAME = 'selfie'
SEARCH_INDEX_NAME = 'euclidean-mongo-search'
VECTOR_SEARCH_INDEX_NAME = 'euclidean-mongo-vector-search'

class MongoDBClient:

    def __init__(self):
        # Connect to MongoDB
        self.client = MongoClient('mongodb+srv://thinpyaiwin:zHNMtTu54da0tIlB@tp-learning-cluster.bil2g.mongodb.net/?retryWrites=true&w=majority&appName=tp-learning-cluster&tlsAllowInvalidCertificates=true', server_api=ServerApi('1')) # MongoClient(f'{PROTOCOL}://{DB_USER_NAME}:{DB_PASSPORT}@{CLUSTER}/?retryWrites=true&w=majority')
        self.db = self.client[DB_NAME]

        # Initialize GridFS
        self.fs = gridfs.GridFS(self.db)

        self.file_helper = FileHelper()


    def create_collection(self) -> Collection:
        """
        Create collection.
        :return: Created Collection
        """
        self.client.admin.command('ping')
        logger.info(f"Successfully connected to MongoDB")

        if SELFIE_COLLECTION_NAME in self.db.list_collection_names():
            logger.warning(f"Collection already exists. Collection : {SELFIE_COLLECTION_NAME}")
            return self.db.get_collection(SELFIE_COLLECTION_NAME)
        try:
            collection = self.db.create_collection(SELFIE_COLLECTION_NAME)
            logger.info(f"Collection is created. Collection : {SELFIE_COLLECTION_NAME}")
            return collection
        except CollectionInvalid:
            logger.error(f"Failure in creating collection. Collection : {SELFIE_COLLECTION_NAME}")
            raise Exception(f"Failure in creating collection. Collection : {SELFIE_COLLECTION_NAME}")

    def create_search_index(self):
        """
        Create MongoDB search index
        :return: Index name
        """
        collection = self.db.get_collection(SELFIE_COLLECTION_NAME)

        # To find embeddings with a specific poi
        if len(list(collection.list_search_indexes(name=POI_INDEX_NAME))) == 0:
            collection.create_index([(POI_INDEX_NAME, 1)], name=POI_INDEX_NAME)
            logger.info(f"Search index for POI is created. Index : {POI_INDEX_NAME}")

        # For cosine search, although MongoDB doesn’t support native high-dimensional vector indexing, a bsic index on embeddings for general management.
        if len(list(collection.list_search_indexes(name=SELFIE_INDEX_NAME))) == 0:
            collection.create_index([(SELFIE_INDEX_NAME, 1)], name=SELFIE_INDEX_NAME ,sparse=True)
            logger.info(f"Search index for EMBEDDING is created. Index : {SELFIE_INDEX_NAME}")

        # Create index for MongoDB vector search
        if len(list(collection.list_search_indexes(name=SEARCH_INDEX_NAME))) == 0:

            vector_search_spec = {
                "name": SEARCH_INDEX_NAME,
                "definition": {
                    "mappings": {
                        "dynamic": False,
                        "fields": {
                            "embedding": {
                                "type": "knnVector",
                                "dimensions": 128,
                                "similarity": "euclidean"
                            },
                            "poi": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
            # dotProduct
            collection.create_search_index(vector_search_spec)
            logger.info(f"Search index for EMBEDDING is created. Index : {SEARCH_INDEX_NAME}")

        # Create index for MongoDB vector search
        if len(list(collection.list_search_indexes(name=VECTOR_SEARCH_INDEX_NAME))) == 0:
            try:
                vector_search_spec = {
                    "name": VECTOR_SEARCH_INDEX_NAME,
                    "definition": {
                        "mappings": {
                            "dynamic": False,
                            "fields": {
                                "embedding": {
                                    "type": "knnVector",
                                    "dimensions": 128,
                                    "similarity": "euclidean"
                                },
                                "poi": {
                                    "type": "token"
                                }
                            }
                        }
                    }
                }
                #
                collection.create_search_index(vector_search_spec)
                logger.info(f"Search index for EMBEDDING is created. Index : {VECTOR_SEARCH_INDEX_NAME}")
            except Exception as e:
                logger.error(f"Failure in creating search index. Index : {VECTOR_SEARCH_INDEX_NAME}, Error : {e}")


    def save_image_and_embedding(self, image_path, poi):
        """
        Save the image to MongoDB
        :return:
        """
        # Step 1: Save the selfie image using GridFS to handle large image files efficiently
        with open(image_path, "rb") as img_f:
            file_name = self.file_helper.get_filename(image_path)
            file_id = self.fs.put(img_f, filename=file_name)
            logger.info(f"Save file. file_name : {file_name}, file_id : {file_id}")

        # Step 2: Generate the embedding for the image
        embedding_vector = generate_embedding(image_path)

        # Step 3: Store the embedding and the reference to the file
        collection = self.db.get_collection(SELFIE_COLLECTION_NAME)
        collection.insert_one({
            "poi": poi,
            "file_id": file_id,
            "file_name": file_name,
            "embedding": embedding_vector.tolist()
        })
        logger.info(f"Save embedding. poi : {poi}, file_id : {file_id}")

    def match_selfie_cosine(self, image_path, poi):

        # input image's embedding vector
        input_embedding = generate_embedding(image_path)

        # Fetch user embeddings from MongoDB by poi
        collection = self.db.get_collection(SELFIE_COLLECTION_NAME)
        stored_embedding_list = list(collection.find({"poi": poi}, {"embedding": 1, "file_name": 1, "poi": 1}))

        # Compare embeddings using cosine similarity
        # -----
        img_file_name, similarity, poi = compare_img_by_cosine(input_embedding, stored_embedding_list)

        if similarity > 0.6:
            logger.info(f'Match. Similarity : {similarity}, selfie : {image_path}, base_img : {img_file_name}, poi : {poi}')

        else:
            logger.warning(f'Unmatch. Similarity : {similarity}, selfie : {image_path}, base_img : {img_file_name}, poi : {poi}')

    def search_selfie(self, image_path, poi):
        # input image's embedding vector
        input_embedding = generate_embedding(image_path)

        # Fetch user embeddings from MongoDB by poi
        collection = self.db.get_collection(SELFIE_COLLECTION_NAME)

        # Compare embeddings using mongo vector search similarity
        results = compare_by_mongo_search(input_embedding, collection, 'poi', poi)


        for result in results:
            similarity = calculate_mongodb_vectore_score(result)
            logger.info(
                f'Match. euclidean-search Similarity : {similarity} : {result['score']}, selfie : {image_path}, base_img : {result['file_name']}, poi : {result['poi']}')

    def vector_search_selfie(self, image_path, poi):
        # input image's embedding vector
        input_embedding = generate_embedding(image_path)

        # Fetch user embeddings from MongoDB by poi
        collection = self.db.get_collection(SELFIE_COLLECTION_NAME)

        # Compare embeddings using mongo vector search similarity
        results = compare_by_mongo_vector_search(input_embedding, collection, 'poi', poi)


        for result in results:
            similarity = calculate_mongodb_vectore_score(result)
            logger.info(
                f'Match. euclidean-vector-search Similarity : {similarity} : {result['score']}, selfie : {image_path}, base_img : {result['file_name']}, poi : {result['poi']}')


    def search_similar_images(self, image_path, top_k=2):

        # input image's embedding vector
        input_embedding = generate_embedding(image_path)

        # Fetch all embeddings from MongoDB
        # TODO NG to load all from DB
        collection = self.db.get_collection(SELFIE_COLLECTION_NAME)
        stored_embedding_list = list(collection.find({}, {"embedding": 1, "poi": 1, "file_id": 1}))

        # Compare embeddings using cosine similarity
        is_match, similarity, poi = compare_img_by_cosine(input_embedding, stored_embedding_list)

        if similarity > 0.9:
            logger.info(f'Match. is_match: {is_match}, similarity : {similarity}')

        else:
            logger.warning(f'Not match. is_match: {is_match}, similarity : {similarity}')







