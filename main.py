from app.card import Card
from app.deck import Deck
from app.hand import Hand
from app.player import Player
from app.game import Game

# creates a deck of 52 cards
deck = Deck()
cards = Card.create_deck_with_52_cards()
deck.add_cards(cards)

# mock game with two players
hand1 = Hand(cards=[])
hand2 = Hand(cards=[])
player1 = Player(name='M', hand=hand1)
player2 = Player(name='Z', hand=hand2)
players = [player1, player2]

# game.play() shuffles deck and deals two cards to x num of players
game = Game(deck=deck, players=players)
game.play()

# # # creates initial three card draw
# # table_hand = []
# # table_count = 0
# # for card in deck.cards:
# #     if table_count < 3:
# #         table_hand.append(card)
# #         deck.remove_cards(card)
# #         table_count += 1

# # draws fourth card

# # draws fifth and final card

# # evaluates hand
# hand = Hand(player_cards)
# # hand = Hand(player_cards + table_hand)
# hand.best_rank()
