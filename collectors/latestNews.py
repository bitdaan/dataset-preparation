import csv
from datetime import datetime
from tools.scraper import getCardList, getCardLatestNews
from classes.cache import save_peak_flag, load_peak_flag, PeakFlag


def collectLatestNews():
    newsList = []
    cardList = []

    for i in range(1, 2):
        print("https://news.bitcoin.com/page/" + str(i) + "/?s")
        cardList = getCardList(
            "https://news.bitcoin.com/page/" + str(i) + "/?s")

    peak = load_peak_flag()

    for card in cardList:
        x = getCardLatestNews(card)
        if peak != None and datetime.fromisoformat(peak.unixTime).timestamp() > datetime.fromisoformat(x.publishedAt).timestamp():
            break
        else:
            newsList.append(x)

    if peak == None or (datetime.fromisoformat(peak.unixTime).timestamp() < datetime.fromisoformat(newsList[0].publishedAt).timestamp()):
        save_peak_flag(PeakFlag(newsList[0].publishedAt))

    with open("latest-news.csv", "w+") as stream:
        writer = csv.writer(stream)
        writer.writerows(newsList)
