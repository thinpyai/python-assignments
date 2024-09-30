from deepface import DeepFace
import numpy as np
from scipy.constants import value
from sklearn.metrics.pairwise import cosine_similarity
import pprint

POI_INDEX_NAME = 'poi'
SEARCH_INDEX_NAME = 'euclidean-mongo-search'
VECTOR_SEARCH_INDEX_NAME = 'euclidean-mongo-vector-search'

def generate_embedding(image_path):
    """
    Generate an embedding from the image
    :param image_path:
    :return:
    """
    embedding_obj = DeepFace.represent(image_path, model_name="Facenet", enforce_detection=False)
    return np.array(embedding_obj[0]["embedding"], dtype=np.float32)

def compare_img_by_cosine(input_embedding, stored_embedding_list):
    """
    Check similarity one by one
    Compute cosine similarity between two embeddings in X and Y.
    :param input_embedding: Input selfie
    :param stored_embedding_list: Stored image in mongoDB
    """
    similarities = []
    for record in stored_embedding_list:
        stored_embedding = np.array(record["embedding"], dtype=np.float32)
        similarity_score = cosine_similarity([input_embedding], [stored_embedding])[0][0]
        similarities.append((record["file_name"], similarity_score, record['poi']))

    best_match = max(similarities, key=lambda x: x[1], default=(None, 0))
    return best_match

def compare_by_mongo_search(input_embedding, collection, key_field=None, key_value=None, num_results=1):

    """
    Search with image by including the matching of part of poi and filter with POI number.
    :param input_embedding:
    :param collection:
    :param key_field:
    :param key_value:
    :param num_results:
    :return:
    """

    # Convert the embedding to a list
    query_embedding = input_embedding.tolist()

    pipeline = [
        {
            "$search": {
                "index": SEARCH_INDEX_NAME,
                "knnBeta": {
                    "vector": query_embedding,
                    "path": "embedding",
                    "k": 100,  # Number of nearest neighbors to return
                    "filter": {
                        "text" : {
                            "path": key_field,
                            "query": key_value
                        }

                    }
                }
            }
        },
        {
            "$match": {
                key_field: key_value  # Exact match filter
            }
        },
        {
            "$project": {
                "embedding": 1,
                "score": {"$meta": "searchScore"},
                "file_name": 1,
                "poi": 1
            }
        },

        {
            "$limit": num_results
        }
    ]

    results = list(collection.aggregate(pipeline))

    return results


def compare_by_mongo_vector_search(input_embedding, collection, key_field=None, key_value=None, num_results=1):
    """
    Search with image by including the matching of part of poi and filter with POI number.
    :param input_embedding:
    :param collection:
    :param key_field:
    :param key_value:
    :param num_results:
    :return:
    """

    # Convert the embedding to a list
    query_embedding = input_embedding.tolist()

    pipeline = [
        {
            "$vectorSearch": {
                "index": VECTOR_SEARCH_INDEX_NAME,
                "path": "embedding",
                "queryVector": query_embedding,
                "numCandidates": 6,
                "limit": 6,
                "filter": {
                    key_field: key_value
                }
            }
        },
        {
            "$project": {
                "embedding": 1,
                "score": {"$meta": "vectorSearchScore"},
                "file_name": 1,
                "poi": 1
            }
        },

        {
            "$limit": num_results
        }
    ]

    results = list(collection.aggregate(pipeline))

    return results

def calculate_mongodb_vectore_score(result):

    # stored_vector = result['embedding']
    score = result['score']
    similarity = 1 / (1 + score)
    return similarity

    # min_score = min(score)
    # max_score = max(score)
    #
    # normalized = (2 * (score - min_score) / (max_score - min_score)) - 1
    # return max(min(normalized, 1), -1)  # Clamp to [-1, 1]



