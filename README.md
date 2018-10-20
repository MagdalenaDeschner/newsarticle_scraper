## Web scraping
- file `scraper.py`
- Scrape german news articles and their category label from www.n-tv.de 
- used packages:
    - `urllib.request` to get http pages
    - `BeautifulSoup` to parse html

## Cleaning and vectorization of text
- file `preprocessing.py`
- clean articles
- use tfidf to vectorize articles into words 
- used packages:
    - `sklearn.feature_extraction.text` to vectorize text with tfidf
    - `XY` XY

## Text classification
- file `classifier.py`
- Train classifier on articles' body and category label to automatically classify future news