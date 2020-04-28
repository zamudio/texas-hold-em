import random


class Deck():
    def __init__(self):
        self.cards = []

    def add_cards(self, new_cards):
        self.cards.extend(new_cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_cards(self, num):
        cards_removed = self.cards[:num]
        del self.cards[:num]
        return cards_removed
