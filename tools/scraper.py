import requests
from bs4 import BeautifulSoup
from classes.news import News

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def getNewsContent(link):
    page = requests.get(link, headers=headers)
    text = ""
    for p in BeautifulSoup(page.content, 'html.parser').find('article', class_='article__body').find_all('p'):
        text = text + " " + p.text
    return text


def getCardList(link):
    page = requests.get(link, headers=headers)
    return BeautifulSoup(page.content, 'html.parser').find(class_="td-ss-main-content").find_all(class_="td_module_16 td_module_wrap td-animation-stack")


def getCardNews(opt):
    title = opt.find('h3', class_="entry-title td-module-title").text
    cat = opt.find('a', class_="td-post-category").text
    link = opt.find(
        'h3', class_="entry-title td-module-title").find('a').get('href')
    publishedAt = opt.find('time').get('datetime')
    return News(title, cat, getNewsContent(link), publishedAt)
