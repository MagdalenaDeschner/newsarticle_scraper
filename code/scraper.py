# Import packages
from bs4 import BeautifulSoup
import pandas as pd
import pickle as pkl
from urllib.request import urlopen, Request

# define links to sport category manually      
sport = ["https://www.n-tv.de/sport/fussball/Mourinho-kaempft-um-seine-Karriere-article20679307.html",
         "https://www.n-tv.de/sport/fussball/Nur-die-Wuerde-des-FC-Bayern-ist-unantastbar-article20679435.html",
         "https://www.n-tv.de/sport/fussball/Gerhard-Delling-kuendigt-bei-der-ARD-article20678453.html",
         "https://www.n-tv.de/sport/Rihanna-will-nicht-beim-Superbowl-singen-article20679903.html",
         "https://www.n-tv.de/sport/formel1/Vettels-WM-Wunder-rueckt-in-weite-Ferne-article20679896.html",
         "https://www.n-tv.de/sport/fussball/Wofuer-Uli-Hoeness-n-tv-attackiert-hat-article20679629.html",
         "https://www.n-tv.de/sport/fussball/Koschinat-bringt-Sandhausen-in-Schwung-article20679682.html",
         "https://www.n-tv.de/sport/fussball/FC-Bayern-greift-deutsche-Medien-an-article20679096.html",
         "https://www.n-tv.de/sport/fussball/Die-heftigsten-Zitate-der-Bayern-Schelte-article20679458.html",
         "https://www.n-tv.de/sport/fussball/Bayerns-Rettertrainer-heisst-Labbadia-article20677437.html",
         "https://www.n-tv.de/sport/fussball/Tic-Tac-Toe-und-Trap-waeren-stolz-article20679247.html",
         "https://www.n-tv.de/sport/formel1/So-rohen-Hunger-kannst-du-nicht-schlagen-article20677252.html",
         "https://www.n-tv.de/sport/formel1/Aus-der-Chancenlosigkeit-greift-Vettel-an-article20675463.html",
         "https://www.n-tv.de/sport/fussball/FC-Bayern-erloest-sich-BVB-tanzt-Stuttgart-weg-article20680365.html",
         "https://www.n-tv.de/sport/fussball/Fuerth-klettert-nach-Aufholjagd-auf-Platz-zwei-article20680319.html",
         "https://www.n-tv.de/sport/fussball/Fuenferpacker-Jovic-euphorisiert-die-Eintracht-article20680170.html",
         "https://www.n-tv.de/sport/fussball/Der-bittere-Rausch-einer-betrogenen-Nacht-article20678813.html"]
   
# define desired category urls
categories = ["https://www.n-tv.de/politik/",
              "https://www.n-tv.de/wirtschaft/",
              #"https://www.n-tv.de/sport/", # loop below doesnt work for sport category
              "https://www.n-tv.de/technik/"]

# set up empty list for articles and links
all_articles = []
all_links = []
all_links.extend(sport)

# loop over categories to get the article links
for category in categories:

    # get all articles per category
    articles = []
    
    # get html page of category
    soup = BeautifulSoup(urlopen(Request(category)).read(),"html.parser")
    
    # get all articles
    article = soup.find_all("article")
    articles.append(article)
    all_articles.append(articles)
    
    # loop over articles to get their links
    links = []
    for article in articles[0]:
        
        # get link of article
        link = article.a.get("href")

        # split link (single token) to one string with several tokens
        link_splitted = " ".join(link.split("/"))
        
        # check if "mediathek" or "thema" are included in link, these are not actual articles
        if link_splitted.find("mediathek")is not -1:
            pass
        elif link_splitted.find("thema") is not -1:
            pass
        else:
            links.append(link)
    
    # append links of category to overall list of links
    all_links.extend(links)

# drop duplicate links 
all_links = set(all_links)
all_links = list(all_links)
print(len(all_links))

# loop over article links to extract category, title and body      
# loop over article links to extract category, title and body      
data = pd.DataFrame()

for idx, link in enumerate(all_links):
    try:
        soup = BeautifulSoup(urlopen(Request(link)).read(), "html.parser")
        article = soup.find("article", attrs={"class":"article box section"})
        
        # get category
        category = article.find("span", attrs={"class":"category"}).text.strip()

        # write category to dataframe
        data.loc[link,"category"] = category    

        # set up empty list for body
        body = []

        # get body
        for paragraph in article.find_all("p"):
            text = paragraph.text.strip()
            body.append(text)
        
        # drop first and last row 
        body = body[1:-1]

        # join paragraphs to one single string
        body = " ".join(body)
        
        # write body to dataframe
        data.loc[link,"body"] = body  

    except:
        pass  
    print(idx)

# write data to pickle
fileObject = open(r"C:\Users\Magdalena Deschner\git_project_newsarticles\articles.p", "wb")
pkl.dump(data, fileObject)
fileObject.close()