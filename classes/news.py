from tools.bitcoin import getBitcoinPrice


class News:
    def __init__(self, title, cat, content, publishedAt):
        self.title = title
        self.cat = cat
        self.content = content
        self.publishedAt = publishedAt
        self.prices = getBitcoinPrice(publishedAt)

    def __repr__(self):
        return f"News({self.title!r}, {self.cat!r}, {self.content!r}, {self.publishedAt!r},{self.prices[0]['priceUsd']!r}, {self.prices[1]['priceUsd']!r}, {self.prices[2]['priceUsd']!r}, {self.prices[3]['priceUsd']!r}, {self.prices[4]['priceUsd']!r}, {self.prices[5]['priceUsd']!r}, {self.prices[6]['priceUsd']!r}, {self.prices[7]['priceUsd']!r}, {self.prices[8]['priceUsd']!r}, {self.prices[9]['priceUsd']!r}, {self.prices[10]['priceUsd']!r}, {self.prices[11]['priceUsd']!r}, {self.prices[12]['priceUsd']!r}, {self.prices[13]['priceUsd']!r}, {self.prices[14]['priceUsd']!r}, {self.prices[15]['priceUsd']!r}, {self.prices[16]['priceUsd']!r}, {self.prices[17]['priceUsd']!r}, {self.prices[18]['priceUsd']!r}, {self.prices[19]['priceUsd']!r}, {self.prices[20]['priceUsd']!r}, {self.prices[21]['priceUsd']!r}, {self.prices[22]['priceUsd']!r}, {self.prices[23]['priceUsd']!r})"

    def __iter__(self):
        return iter([self.title, self.cat, self.content, self.publishedAt, self.prices[0]["priceUsd"], self.prices[1]["priceUsd"], self.prices[2]["priceUsd"], self.prices[3]["priceUsd"], self.prices[4]["priceUsd"], self.prices[5]["priceUsd"], self.prices[6]["priceUsd"], self.prices[7]["priceUsd"], self.prices[8]["priceUsd"], self.prices[9]["priceUsd"], self.prices[10]["priceUsd"], self.prices[11]["priceUsd"], self.prices[12]["priceUsd"], self.prices[13]["priceUsd"], self.prices[14]["priceUsd"], self.prices[15]["priceUsd"], self.prices[16]["priceUsd"], self.prices[17]["priceUsd"], self.prices[18]["priceUsd"], self.prices[19]["priceUsd"], self.prices[20]["priceUsd"], self.prices[21]["priceUsd"], self.prices[22]["priceUsd"], self.prices[23]["priceUsd"]])
