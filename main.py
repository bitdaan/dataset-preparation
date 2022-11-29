import csv
from tools.scraper import getCardList, getCardNews


newsList = []

startPage = 1
endPage = 2 #since i've written this code, news.bitcoin.com has 2407 pages. So, if U wanna scrap all that change this to 2407 :)

for i in range(startPage, endPage):
    cardList = getCardList("https://news.bitcoin.com/page/" + str(i) + "/?s")
    for card in cardList:
        newsList.append(getCardNews(card))


with open("data-set.csv", "w+") as stream:
    writer = csv.writer(stream)
    writer.writerows(newsList)
