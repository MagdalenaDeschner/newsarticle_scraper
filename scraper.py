# Import packages
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# Specify the url
url = "https://www.n-tv.de/sport/fussball/Nur-die-Wuerde-des-FC-Bayern-ist-unantastbar-article20679435.html"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# get text of response
html = response.read()

# print html
soup = BeautifulSoup(html, "html.parser")

# get article
article = soup.find("article", attrs={"class":"article box section"})

# get category and title 
category = article.find("span", attrs={"class":"category"}).text.strip()
title = article.find("h1").text.strip()

# get body
body = article.find_all("p")

bodytext = []
for paragraph in body:
    text = paragraph.text.strip()
    bodytext.append(text)
bodytext = bodytext[1:-1]
body = " ".join(bodytext)

# Be polite and close the response!
response.close()