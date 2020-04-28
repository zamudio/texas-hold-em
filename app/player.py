class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def best_hand(self):
        # using dependency injection to avoid hard coupling the hand class to the player class
        return self.hand.best_rank()
