## How to setup
```
git clone https://github.com/sayansaha934/wikipedia-analysis.git
cd wikipedia-analysis
conda create -n venv python==3.8 --y
conda activate venv
pip install -r requirements.txt
uvicorn main:app --reload
```
## Example
### Word Frequency Analysis Endpoint
- Request:
   ```
   curl -X 'GET' \
  'http://127.0.0.1:8000/word-frequency-analysis/?topic=COVID-19&n=3' \
  -H 'accept: application/json'
   ```
- Response:
```
{
  "topic": "COVID-19",
  "top_words": [
    ["people", 67],
    ["may", 54],
    ["virus", 52]
  ]
}

```
### Search History Endpoint
- Request
  ```
  curl -X 'GET' \
  'http://127.0.0.1:8000/search-history/' \
  -H 'accept: application/json'
  ```
- Response
  ```
  [
  {
    "topic": "COVID-19",
    "top_words": [
      ["people", 67],
      ["may", 54],
      ["virus", 52]
    ]
  },
  {
    "topic": "Malnutrition",
    "top_words": [
      ["food", 102],
      ["malnutrition", 79],
      ["children", 55]
    ]
  }]
  ```
## Run test cases
`python test.py`
