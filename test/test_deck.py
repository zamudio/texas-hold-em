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

    # def test_deck_removes_card_from_its_collection(self):
    #     card = Card(rank='Ace', suit='Spades')
    #     deck = Deck()
    #     deck_of_cards = Card.create_deck_with_52_cards()
    #     deck.add_cards(deck_of_cards)
    #     deck.remove_card([card])

    #     assert deck.cards != [card]
