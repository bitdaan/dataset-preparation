from datetime import datetime
import os
from tools.scraper import getCardList, getCardNews
from classes.cache import *


def createDataset(startPage, endPage, newsList, path):
    cardList = []

    for i in range(startPage, endPage):
        cardList = getCardList(
            "https://news.bitcoin.com/page/" + str(i) + "/?s")
        save_continue_date(ContinueDate(i, endPage, path))
        print("https://news.bitcoin.com/page/" + str(i) + "/?s")
        for card in cardList:
            newsList.append(getCardNews(card))

    peak = load_peak_flag()

    if peak == None or (datetime.fromisoformat(peak.unixTime).timestamp() < datetime.fromisoformat(newsList[0].publishedAt).timestamp()):
        save_peak_flag(PeakFlag(newsList[0].publishedAt))


def continueCreateDataset(newsList, x):
    if x != None and int(x.startPage)+1 != int(x.endPage) and os.path.exists(x.path) == True:
        createDataset(x.startPage, x.endPage, newsList, x.path)
    else:
        print("Last duration had been ended or saving path is not valid.")
