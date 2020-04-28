from app.card import Card
from app.deck import Deck
from app.hand import Hand
from app.player import Player

# creates a deck of 52 cards
deck = Deck()
deck_of_cards = Card.create_deck_with_52_cards()
deck.add_cards(deck_of_cards)

hand1 = Hand(cards=[])
player1 = Player(name='M', hand=hand1)

# # creates a player hand with two cards from the deck created above
# player_cards = []
# player_count = 0
# for card in deck.cards:
#     if player_count < 2:
#         player_cards.append(card)
#         # deck.remove_card(card)
#         player_count += 1

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
