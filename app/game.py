class Game():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def play(self):
        self.deck.shuffle()

        for player in self.players:
            cards = self.deck.remove_cards(2)
            player.hand.cards.extend(cards)
