import pytest    # importing test framework
# inside app folder, locate card.py and import whole class called Card from that file
from app.card import Card


class TestCard:
    def test_card_has_rank(self):
        card = Card(rank='Queen', suit='Hearts')
        assert card.rank == 'Queen'

    def test_card_has_suit(self):
        card = Card(rank='2', suit='Spades')
        assert card.suit == 'Spades'

    def test_card_has_string_representation_with_rank_and_suit(self):
        card = Card('3', 'Diamonds')
        assert str(card) == '3 of Diamonds'

    def test_card_has_one_of_four_possible_suit_options(self):
        assert Card.SUITS == ('Hearts', 'Clubs', 'Spades', 'Diamonds')

    def test_card_has_one_of_thirteen_possible_rank_options(self):
        assert Card.RANKS == ('2', '3', '4', '5', '6', '7',
                              '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

    def test_card_only_allows_valid_rank(self):
        with pytest.raises(ValueError):
            Card(rank='Two', suit='Clubs')

    def test_card_only_allows_valid_suit(self):
        with pytest.raises(ValueError):
            Card(rank='2', suit='Peanut Butter')
