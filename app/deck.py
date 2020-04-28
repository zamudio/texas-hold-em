import random


class Deck():
    def __init__(self):
        self.cards = []

    def add_cards(self, new_cards):
        self.cards.extend(new_cards)

    def shuffle(self):
        random.shuffle(self.cards)

    # def remove_card(self, card):
    #     self.cards.remove(card)
