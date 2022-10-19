import csv
from tools.news import getNews


with open("data.csv", "w") as stream:
    writer = csv.writer(stream)
    writer.writerows(getNews([]))
