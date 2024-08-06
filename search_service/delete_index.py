from src.elastic_client import elastic_search_client
from src.config import ELASTIC_SEARCH_INDEX_NAME


def delete_index(index_name):
    elastic_search_client.indices.delete(index=index_name)


delete_index(index_name=ELASTIC_SEARCH_INDEX_NAME)
