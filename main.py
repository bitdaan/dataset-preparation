"""Bitdaan Dataset Preparation.

For dataset preparation, pass args like this:
    python main --collect dataset --start-page 1 --end-page 2407 --path /home/user/Desktop

For continue dataset preparation, pass args like this:
    python main --collect continue 

For just collect latest news which are not in dataset and did not analyze by bitdaan, pass args like this:
    python main --collect latest --path /home/user/Desktop

Usage:
    bitdaan [--collect=TYPE] [--start-page=NUMBER] [--end-page=NUMBER] [--path=PATH]
    
"""

import docopt
import os
import csv
import atexit
from collectors.news import *
from collectors.latestNews import *
from classes.cache import load_continue_date

newsList = []
latestNewsList = []
path = ""


def exit_handler():
    global newsList, latestNewsList, path
    if len(newsList) > 0:
        with open(path + "/data-set.csv", "a") as stream:
            writer = csv.writer(stream)
            writer.writerows(newsList)
    elif len(latestNewsList) > 0:
        with open(path + "/latest-news.csv", "a") as stream:
            writer = csv.writer(stream)
            writer.writerows(latestNewsList)


atexit.register(exit_handler)


def main():
    global newsList, latestNewsList, path
    args = docopt.docopt(__doc__)
    if args['--collect'] == "dataset":
        if args['--start-page'] != None and args['--end-page'] != None and args['--path'] != None and os.path.exists(args['--path']) == True:
            if os.path.exists(args['--path'] + "/data-set.csv"):
                os.remove(args['--path'] + "/data-set.csv")
            if os.path.exists("pickles/peak-flag.pickle"):
                os.remove("pickles/peak-flag.pickle")
            if os.path.exists("pickles/continue-date.pickle"):
                os.remove("pickles/continue-date.pickle")
            path = args['--path']
            createDataset(int(args['--start-page']),
                          int(args['--end-page']), newsList, args['--path'])
        else:
            exit('Error !\n\trun " python main.py -h " for more help.')
    elif args['--collect'] == "continue":
        x = load_continue_date()
        path = x.path
        continueCreateDataset(newsList, x)
    elif args['--collect'] == "latest" and args['--path'] != None and os.path.exists(args['--path']) == True:
        path = args['--path']
        collectLatestNews(latestNewsList)
    else:
        exit('Error !\n\trun " python main.py -h " for more help.')


if __name__ == '__main__':
    main()
