from app.card import Card
from app.deck import Deck

deck = Deck()
cards = Card.create_deck_with_52_cards()
deck.add_cards(cards)
