import requests
from collections import Counter
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk

# Download NLTK stopwords data
nltk.download("stopwords")


def get_wikipedia_text(topic):
    """
    Fetch the text content of a Wikipedia article for the given topic.

    Parameters:
    - topic (str): The topic for which the Wikipedia article should be fetched.

    Returns:
    - str: The text content of the Wikipedia article, or None if an error occurs.
    """
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": topic,
        "format": "json",
        "prop": "text",
        "redirects": "",
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()

        raw_html = data["parse"]["text"]["*"]
        soup = BeautifulSoup(raw_html, "html.parser")
        soup.find_all("p")
        text = ""

        for p in soup.find_all("p"):
            text += p.text
        return text
    except Exception:
        return None


def analyze_word_frequency(text, n):
    """
    Analyze the word frequency in the given text.

    Parameters:
    - text (str): The text content for word frequency analysis.
    - n (int): The number of top words to retrieve.

    Returns:
    - list: A list of tuples containing the most common words and their frequencies.
    """
    words = text.split()
    stop_words = set(stopwords.words("english"))

    # Filter out stopwords and non-alphabetic words
    filtered_words = [
        word.lower()
        for word in words
        if word.isalpha() and word.lower() not in stop_words
    ]
    word_frequency = Counter(filtered_words)
    return word_frequency.most_common(n)
