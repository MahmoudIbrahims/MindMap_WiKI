![Wiki](https://github.com/MahmoudIbrahims/MindMap_WiKI/assets/121377479/2c86afe4-4bd2-4381-9b7e-cf253443bfd2)

# MindMap Wiki

MindMap Wiki is a Streamlit application that leverages the power of language models and Wikipedia to provide detailed responses to user queries. The app uses the LangChain framework and integrates with Google Generative AI to deliver accurate and insightful information.

## Features

- **Interactive Search**: Users can enter their search queries to get detailed responses.
- **Integration with Wikipedia**: The app uses Wikipedia as a primary source for information retrieval.
- **Advanced Language Model**: Utilizes Google Generative AI (gemini-pro model) for generating responses.
- **Mathematical Tools**: Includes tools for performing mathematical calculations.
- **User-Friendly Interface**: Simple and intuitive interface powered by Streamlit.

## Prerequisites

To run this application, you need to have the following installed:

- Python 3.7 or later
- Streamlit
- LangChain
- langchain_google_genai
- IPython

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/mindmap-wiki.git
    cd mindmap-wiki
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up your Google API key:

    Replace `"Api_key"` with your actual Google API key in the `google_api_key` variable in the `app.py` file.

## Running the App

To start the Streamlit application, run:

```sh
streamlit run app.py
