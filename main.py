import random
from app.card import Card
from app.deck import Deck

deck = Deck()
cards = Card.create_deck_with_52_cards()
deck.add_cards(cards)


random_deal = cards.random.randint(0, 52)

# for card in cards:
#     print(card)

# dealt_cards = {
#     Card[random_deal] =
# }

# hand = Hand(cards)

deck.remove_cards(random_deal)
