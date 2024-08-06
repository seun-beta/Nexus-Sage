from openai import OpenAI

from search_service.query_index import retrieve_answer


openai_client = OpenAI()


def rag_client(user_query):
    answer = retrieve_answer(user_query)

    system_message = """
        You are a Retrieval-Augmented Generation (RAG) system designed for Nexus Inc., 
        founded in 2012. Your primary function is to assist with the employee handbook by 
        retrieving relevant information and generating accurate and helpful responses based on the handbook's content. 
        Do not use markdown when answering the question. Also, keep responses to 60 words maximum
        """

    prompt = f"""
        Based on the retrieved information from Nexus Inc.'s employee handbook, 
        please provide a detailed and accurate response to the following query:

        Query: {user_query}

        Retrieved Information:

    {answer}
        Select the most relevant information from the retrieved results that directly 
        addresses the user's query. If none of the results are relevant or if the query 
        is not related to HR policies for Nexus Inc., return something like 
        ``Sorry I cannot find any information that matches your question``. Feel free to be creative.
        """

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.7,
        max_tokens=500,
        top_p=1,
    )
    return response.choices[0].message.content
