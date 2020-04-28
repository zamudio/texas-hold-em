import pytest
from unittest.mock import patch
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

    @patch('random.shuffle')
    def test_desk_shuffles_cards(self, mock_shuffle):
        deck = Deck()
        cards = [
            Card(rank='7', suit='Diamonds'),
            Card(rank='3', suit='Spades')
        ]
        deck.add_cards(cards)
        deck.shuffle()

        assert mock_shuffle.called_once_with(cards)

    def test_deck_removes_cards_from_its_collection(self):
        card1 = Card(rank='Ace', suit='Spades')
        card2 = Card(rank='4', suit='Diamonds')
        cards = [card1, card2]

        deck = Deck()
        deck.add_cards(cards)

        assert deck.remove_cards(1) == [card1]
        assert deck.cards == [card2]
