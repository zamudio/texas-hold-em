import pytest    # importing test framework
from app.card import Card
# inside app folder, locate card.py and import whole class called Card from that file


class TestCard:
    def test_card_has_rank(self):
        card = Card(rank='Queen', suit='Hearts')
        assert card.rank == 'Queen'

    def test_card_has_suit(self):
        card = Card(rank='2', suit='Spades')
        assert card.suit == 'Spades'

    def test_card_knows_its_rank_index(self):
        card = Card(rank='Queen', suit='Hearts')
        assert card.rank_index == 10

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

    def test_card_can_create_deck_with_52_cards(self):
        cards = Card.create_deck_with_52_cards()
        assert len(cards) == 52
        assert cards[0] == Card(rank='2', suit='Hearts')
        assert cards[-1] == Card(rank='Ace', suit='Diamonds')

    def test_card_can_check_if_two_cards_are_equal(self):
        assert Card(rank='2', suit='Hearts') == Card(rank='2', suit='Hearts')

    def test_if_card_is_less_than_other_card(self):
        queen_of_hearts = Card(rank='Queen', suit='Hearts')
        king_of_hearts = Card(rank='King', suit='Hearts')
        evaluate = queen_of_hearts < king_of_hearts
        assert evaluate == True

    def test_cards_are_sorted(self):
        ace_of_hearts = Card(rank='Ace', suit='Hearts')
        six_of_spades = Card(rank='6', suit='Spades')
        six_of_hearts = Card(rank='6', suit='Hearts')
        nine_of_diamonds = Card(rank='9', suit='Diamonds')
        ten_of_clubs = Card(rank='10', suit='Clubs')

        cards = [
            ace_of_hearts,
            nine_of_diamonds,
            six_of_spades,
            ten_of_clubs,
            six_of_hearts
        ]

        cards.sort()
        assert cards == [
            six_of_spades,
            six_of_hearts,
            nine_of_diamonds,
            ten_of_clubs,
            ace_of_hearts
        ]
