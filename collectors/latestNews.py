from datetime import datetime
from tools.scraper import getCardList, getCardLatestNews
from classes.cache import save_peak_flag, load_peak_flag, PeakFlag


def collectLatestNews(newsList):
    cardList = []
    peak = load_peak_flag()

    for i in range(1, 3):
        print("https://news.bitcoin.com/page/" + str(i) + "/?s")
        cardList = getCardList(
            "https://news.bitcoin.com/page/" + str(i) + "/?s")
        for card in cardList:
            x = getCardLatestNews(card)
            if peak != None and datetime.fromisoformat(peak.unixTime).timestamp() > datetime.fromisoformat(x.publishedAt).timestamp():
                break
            else:
                newsList.append(x)

    if peak == None or (datetime.fromisoformat(peak.unixTime).timestamp() < datetime.fromisoformat(newsList[0].publishedAt).timestamp()):
        save_peak_flag(PeakFlag(newsList[0].publishedAt))
