import csv
from tools.scraper import getCardList, getCardNews
from classes.cache import *


def createDataset(startPage, endPage):
    newsList = []
    cardList = []

    for i in range(startPage, endPage):
        print("https://news.bitcoin.com/page/" + str(i) + "/?s")
        save_continue_date(ContinueDate(i, endPage))
        cardList = getCardList(
            "https://news.bitcoin.com/page/" + str(i) + "/?s")

    for card in cardList:
        newsList.append(getCardNews(card))

    if load_peak_flag() == None or (load_peak_flag().unixTime < newsList[0].publishedAt):
        save_peak_flag(PeakFlag(newsList[0].publishedAt))

    with open("data-set.csv", "w+") as stream:
        writer = csv.writer(stream)
        writer.writerows(newsList)


def continueCreateDataset():
    x = load_continue_date()
    if x != None and int(x.startPage)+1 != int(x.endPage):
        createDataset(x.startPage, x.endPage)
    else:
        print("Last duration had been ended.")
