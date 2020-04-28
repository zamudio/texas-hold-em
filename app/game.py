
# will need deck and players, .play, .end


class Game():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def play(self):
        # shuffle the deck
        self.deck.shuffle()
        # hand out two cards for each player
