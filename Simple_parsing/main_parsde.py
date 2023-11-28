import requests
from bs4 import BeautifulSoup
#We added a "while True" for makind this infinite
while True:
    name1 = input("enter a category: ")

    if name1 == "weak":
#start parsing
        CATEGORY="igri-dly-slabih-pc/"
        URL="https://itorrents-igruha.org/igri-dly-slabih-pc/" + CATEGORY

        html = requests.get(URL).text
        soup = BeautifulSoup(html, "html.parser")
        games = soup.find_all('div', class_="article-film")

        for name in games:
            title = name.find('center').get_text()
            print(title)
#starting parsing №2 for top 10 online games
    elif name1 == "online10":
        CATERGORY1="top10-online.html"
        URL1="https://itorrents-igruha.org/" + CATERGORY1

        html1 = requests.get(URL1).text
        soup1 = BeautifulSoup(html1, "html.parser")
        games1 = soup1.find_all('div', class_="short-item22 rel-item22")

        for namess in games1:
            title2 = namess.find("a", class_="act-item32").get_text()
            print(title2)
#if something went wrong
    else:
        print("Error 404!")


