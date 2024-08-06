<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/ET4L2XV.png" alt="Project logo"></a>
</p>

<h3 align="center">Nexus Sage</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/seun-beta/nexus-sage.svg)](https://github.com/seun-beta/nexus-sage/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/seun-beta/nexus-sage.svg)](https://github.com/seun-beta/nexus-sage/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Nexus Sage is a Retrieval-Augmented Generation (RAG) system designed to assist with retrieving relevant information from Nexus Inc.'s employee handbook and generating accurate responses based on the handbook's content.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Testing](#testing)
- [Built Using](#built_using)
- [Contributing](#contributing)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)

## 🧐 About <a name = "about"></a>

Nexus Sage is designed to provide quick and accurate responses to queries related to Nexus Inc.'s employee handbook. By leveraging Elasticsearch for data storage and retrieval and OpenAI's GPT for response generation, Nexus Sage ensures that employees can access the information they need efficiently.

The project consists of several components:
- A FastAPI server that handles incoming requests and routes them to the appropriate services.
- An Elasticsearch instance that stores the employee handbook data and supports efficient querying.
- An integration with OpenAI's GPT model to generate responses based on the retrieved data.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- Elasticsearch instance
- OpenAI API key

### Installing

1. **Clone the repository:**
    ```bash
    git clone https://github.com/seun-beta/nexus-sage.git
    cd nexus-sage
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables in a `.env` file:**
    ```plaintext
    ELASTIC_SEARCH_HOST=<your_elasticsearch_host>
    ELASTIC_SEARCH_USER=<your_elasticsearch_username>
    ELASTIC_SEARCH_PASSWORD=<your_elasticsearch_password>
    ELASTIC_SEARCH_INDEX_NAME=nexus_sage
    OPENAI_API_KEY=<your_openai_api_key>
    ```

### Elasticsearch Setup

1. **Create the Elasticsearch index:**
    ```bash
    python create_index.py
    ```

2. **Load data into the Elasticsearch index:**
    ```bash
    python load_data.py
    ```

3. **(Optional) Delete the Elasticsearch index:**
    ```bash
    python delete_index.py
    ```

## 🎈 Usage <a name="usage"></a>

To use the system, start the FastAPI server and interact with the endpoints.

1. **Start the FastAPI server:**
    ```bash
    uvicorn api:app --reload
    ```

2. **The API will be available at `http://127.0.0.1:8000`.**

### Endpoints

- **Health Check:** `GET /`
  - Returns: `{"data": "PONG!"}`

- **Query:** `POST /query`
  - Request Body:
    ```json
    {
      "query": "Your question here"
    }
    ```
  - Returns: `{"data": "Generated response based on the handbook"}`

## 🔧 Testing <a name = "testing"></a>

To ensure that the system is working correctly, you can run the automated tests provided.

### Coding style tests

Ensure that the code adheres to the required coding standards and practices.

```bash
flake8 .  # Check for PEP 8 compliance
```

## ⛏️ Built Using <a name = "built_using"></a>

- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework
- [Elasticsearch](https://www.elastic.co/elasticsearch/) - Search Engine
- [OpenAI](https://openai.com/) - AI Model

## 🤝 Contributing <a name = "contributing"></a>

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ✍️ Authors <a name = "authors"></a>

- [@seun-beta](https://github.com/seun-beta) - Development

## 🎉 Acknowledgements <a name = "acknowledgements"></a>

- Thanks to [DataTalksClub](https://datatalks.club/) for the LLM Zoomcamp and inspiration.
- Inspiration and support from the open-source community.
# nexus-sage
