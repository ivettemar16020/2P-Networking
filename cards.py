symbols = ["Heart", "Diamond", "Spade", "Club"]

class Card:
    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol
    def getNameForImage(self):
        card_name = str(self.value) + self.symbol
        if card_name[1].isdigit():
            return card_name[0:3]
        else:
            return card_name[0:2]
def generate_deck():
    deck = []
    for value in (list(range(2, 11)) + ["A", "J", "Q", "K"]):
        for symbol in symbols:
            deck.append(Card(value, symbol))

    return deck
