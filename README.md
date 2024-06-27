# News Search Agent

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)


## Overview

The News Search Agent allows users to search for news articles based on their queries using Google Search API wrapped in LangChain. This app provides a simple and intuitive interface for users to discover the latest news on topics of interest.

## Features

- **Search Functionality**: Enter a query related to news topics and retrieve relevant articles.
- **Dynamic Updates**: Results are updated dynamically based on user input.
- **Error Handling**: Displays errors if articles cannot be fetched or parsed correctly.
- **API Integration**: Utilizes Google Search API and LangChain for fetching and parsing news articles.

## Screenshots

<div style="display: flex; flex-direction: row;">
    <img width="400" alt="Screenshot 2024-06-27 165557" src="https://github.com/abhikalparya/news-search-agent/assets/81465377/3831120e-b945-4bce-8645-95639583e6cf">
    <img width="400" alt="Screenshot 2024-06-27 165808" src="https://github.com/abhikalparya/news-search-agent/assets/81465377/fe1ad244-e6a6-4de0-acf7-906a2dae9003">
</div>

<div style="display: flex; flex-direction: row;">
    <img width="400" alt="Screenshot 2024-06-27 165712" src="https://github.com/abhikalparya/news-search-agent/assets/81465377/5422d6cf-f823-4481-91af-3ddbe9c2d9f0">
    <img width="400" alt="Screenshot 2024-06-27 165848" src="https://github.com/abhikalparya/news-search-agent/assets/81465377/0496fa00-40ed-40da-a964-6a94e8164f6a">
</div>


### Prerequisites

- Python 3.6+
- Streamlit: Install using `pip install streamlit`
- Required Libraries: Install using `pip install langchain_community langchain_core newspaper3k`

### Environment Variables

Before running the app, make sure to set the following environment variables:

- `GOOGLE_CSE_ID`: Google Custom Search Engine ID
- `GOOGLE_API_KEY`: Google API Key for Custom Search
- `OPENAI_API_KEY`: OpenAI API Key for accessing GPT-3 models


