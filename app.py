import os
import streamlit as st
from openai import OpenAI
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool
from newspaper import Article, Config, ArticleException

# Set up environment variables
os.environ["GOOGLE_CSE_ID"] = "YOUR_CSE_ID"
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Function to fetch and parse news articles
def fetch_and_parse_article(url):
    try:
        config = Config()
        config.browser_user_agent = (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )

        article = Article(url, config=config)
        article.download()
        article.parse()

        if article.text and len(article.text) > 100:
            return {
                "title": article.title,
                "link": article.url,
            }
        else:
            return None
    except ArticleException as e:
        st.error(f"Failed to fetch article from {url}: {e}")
        return None

# Function to fetch top news results
def top_news_results(query, num_results=5):
    search_results = search.results(f"{query} latest news 'this week'", num_results) 
    articles = []
    for result in search_results:
        article_content = fetch_and_parse_article(result['link'])
        if article_content:
            articles.append(article_content)
    return articles

# Set up Google Search tool
search = GoogleSearchAPIWrapper()
tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=top_news_results,
)

# Function to search for news articles using LangChain's Google Search tool
def search_news_with_langchain(query):
    search_results = tool.func(query)
    return search_results

# Function to get news articles based on a user query
def get_news_articles(query):
    search_results = search_news_with_langchain(query)

    articles = []
    for result in search_results:
        if 'link' in result:
            article_content = fetch_and_parse_article(result['link'])
            if article_content:
                articles.append(article_content)

    return articles

# Streamlit app UI
def main():
    st.title("News Search Agent")

    query = st.text_input("Enter your news query:")
    if st.button("Search"):
        if query:
            results = get_news_articles(query)
            if results:
                for idx, article in enumerate(results, start=1):
                    st.subheader(f"{idx}. {article['title']}")
                    st.write(f"Link: {article['link']}")
                    st.markdown("---")
            else:
                st.write("No news articles found.")

if __name__ == "__main__":
    main()