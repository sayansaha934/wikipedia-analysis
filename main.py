from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from utils import get_wikipedia_text, analyze_word_frequency

app = FastAPI()

# Maintain a list to store search history
search_history = []


@app.get("/word-frequency-analysis/")
async def word_frequency_analysis(topic: str, n: int):
    """
    Endpoint for word frequency analysis of a Wikipedia article.

    Parameters:
    - topic (str): The topic for which the word frequency analysis should be performed.
    - n (int): The number of top words to retrieve.

    Returns:
    - dict: A dictionary containing the topic and the list of top words with their frequencies.
    """
    text = get_wikipedia_text(topic)

    if not text:
        raise HTTPException(
            status_code=404, detail="Wikipedia article not found for the given topic"
        )

    top_words = analyze_word_frequency(text, n)

    # Record the search history
    search_history.append({"topic": topic, "top_words": top_words})

    return {"topic": topic, "top_words": top_words}


@app.get("/search-history/")
async def search_history_endpoint():
    """
    Endpoint for retrieving the search history.

    Returns:
    - JSONResponse: A JSON response containing the search history.
    """
    return JSONResponse(content=search_history)
