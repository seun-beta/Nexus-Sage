from src.elastic_client import elastic_search_client
from src.config import ELASTIC_SEARCH_INDEX_NAME

index_settings = {
    "settings": {"number_of_shards": 1, "number_of_replicas": 0},
    "mappings": {
        "properties": {"question": {"type": "text"}, "answer": {"type": "text"}}
    },
}


def create_index():
    elastic_search_client.indices.create(
        index=ELASTIC_SEARCH_INDEX_NAME, body=index_settings
    )


create_index()
