import json

from src.elastic_client import elastic_search_client
from src.config import ELASTIC_SEARCH_INDEX_NAME


def load_data():
    with open("data.handbook.json") as handbook:
        document = json.load(handbook)

    from elasticsearch.helpers import bulk

    actions = [
        {"_index": ELASTIC_SEARCH_INDEX_NAME, "_source": doc} for doc in document
    ]

    bulk(elastic_search_client, actions)


load_data()
