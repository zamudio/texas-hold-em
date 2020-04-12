import pytest
from app.deck import Deck
from app.card import Card


class TestDeck:
    def test_deck_stores_no_cards_at_start(self):
        deck = Deck()
        assert deck.cards == []

    def test_deck_adds_cards_to_its_collection(self):
        card = Card(rank='Jack', suit='Diamonds')
        deck = Deck()
        deck.add_cards([card])

        assert deck.cards == [card]

    def test_deck_removes_cards_from_its_collection(self):
        card = Card(rank='Ace', suit='Spades')
        deck = Deck()
        deck.add_cards([card])
        deck.remove_cards([card])

        assert deck.cards != [card]
