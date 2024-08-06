from src.elastic_client import elastic_search_client
from src.config import ELASTIC_SEARCH_INDEX_NAME


def retrieve_answer(user_question):
    search_query = {"query": {"match": {"question": user_question}}}

    result = elastic_search_client.search(
        index=ELASTIC_SEARCH_INDEX_NAME, body=search_query
    )
    answers = [hit["_source"] for hit in result["hits"]["hits"]]

    context = ""

    for answer in answers:
        context += answer["answer"]
    return context
