from tools.bitcoin import getPrice
from datetime import datetime, timedelta


class News:
    def __init__(self, title, description, content, publishedAt):
        self.title = title
        self.description = description
        self.content = content
        self.publishedAt = publishedAt
        self.zero = getPrice(
            datetime.fromisoformat(publishedAt[:-1] + '+00:00'))
        self.one = getPrice(
            datetime.fromisoformat(publishedAt[:-1] + '+00:00') + timedelta(hours=1))
        self.three = getPrice(
            datetime.fromisoformat(publishedAt[:-1] + '+00:00') + timedelta(hours=3))
        self.six = getPrice(
            datetime.fromisoformat(publishedAt[:-1] + '+00:00') + timedelta(hours=6))
        self.nine = getPrice(
            datetime.fromisoformat(publishedAt[:-1] + '+00:00') + timedelta(hours=9))
        self.tweleve = getPrice(
            datetime.fromisoformat(publishedAt[:-1] + '+00:00') + timedelta(hours=12))

    def __repr__(self):
        return f"News({self.title!r}, {self.description!r}, {self.content!r}, {self.publishedAt!r}, {self.zero!r}, {self.one!r}, {self.three!r}, {self.six!r}, {self.nine!r}, {self.tweleve!r})"

    def __iter__(self):
        return iter([self.title, self.description, self.content, self.publishedAt, self.zero, self.one, self.three, self.six, self.nine, self.tweleve])
