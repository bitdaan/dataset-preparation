from tools.bitcoin import getBitcoinPrice


class LatestNews:
    def __init__(self, title, cat, content, publishedAt):
        self.title = title
        self.cat = cat
        self.content = content
        self.publishedAt = publishedAt

    def __repr__(self):
        return f"News({self.title!r}, {self.cat!r}, {self.content!r}, {self.publishedAt!r})"

    def __iter__(self):
        return iter([self.title, self.cat, self.content, self.publishedAt])
