import pytest
from app.hand import Hand
from app.card import Card


class TestHand:
    def test_hand_recieves_and_stores_cards(self):
        cards = [
            Card(rank='Queen', suit='Hearts'),
            Card(rank='3', suit='Diamonds')
        ]

        hand = Hand(cards=cards)
        assert hand.cards == cards

    def test_hand_figures_out_no_cards_is_best_rank(self):
        hand = Hand(cards=[])

        assert hand.best_rank() == 'No Cards'

    def test_hand_figures_out_high_card_is_best_rank(self):
        cards = [
            Card(rank='Ace', suit='Clubs'),
            Card(rank='6', suit='Spades')
        ]

        hand = Hand(cards=cards)
        assert hand.best_rank() == 'High Card'

    def test_hand_figures_out_single_pair_is_best_rank(self):
        cards = [
            Card(rank='Jack', suit='Spades'),
            Card(rank='4', suit='Clubs'),
            Card(rank='7', suit='Diamonds'),
            Card(rank='King', suit='Diamonds'),
            Card(rank='7', suit='Hearts')
        ]

        hand = Hand(cards=cards)
        assert hand.best_rank() == 'Pair'

    def test_hand_figures_out_two_pair_is_best_rank(self):
        cards = [
            Card(rank='Ace', suit='Spades'),
            Card(rank='9', suit='Clubs'),
            Card(rank='7', suit='Diamonds'),
            Card(rank='Ace', suit='Diamonds'),
            Card(rank='7', suit='Hearts')
        ]

        hand = Hand(cards=cards)
        assert hand.best_rank() == 'Two Pair'

    def test_hand_figures_out_three_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank='7', suit='Spades'),
            Card(rank='King', suit='Clubs'),
            Card(rank='7', suit='Diamonds'),
            Card(rank='3', suit='Diamonds'),
            Card(rank='7', suit='Hearts')
        ]

        hand = Hand(cards=cards)
        assert hand.best_rank() == 'Three of a Kind'

    def test_hand_figures_out_straight_is_best_rank(self):
        cards = [
            Card(rank='3', suit='Hearts'),
            Card(rank='4', suit='Spades'),
            Card(rank='5', suit='Hearts'),
            Card(rank='6', suit='Diamonds'),
            Card(rank='7', suit='Clubs')
        ]

        hand = Hand(cards=cards)
        assert hand.best_rank() == 'Straight'

    def test_hand_figures_out_flush_is_best_rank(self):
        cards = [
            Card(rank=rank, suit='Diamonds')
            for rank in ['2', '5', '8', '10', 'Ace']
        ]

        hand = Hand(cards=cards)
        assert hand.best_rank() == 'Flush'

    def test_hand_figures_out_full_house_is_best_rank(self):
        cards = [
            Card(rank='3', suit='Clubs'),
            Card(rank='3', suit='Hearts'),
            Card(rank='3', suit='Diamonds'),
            Card(rank='9', suit='Spades'),
            Card(rank='9', suit='Diamonds')
        ]

        hand = Hand(cards=cards)
        assert hand.best_rank() == 'Full House'

    def test_hand_figures_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank='7', suit='Spades'),
            Card(rank='King', suit='Clubs'),
            Card(rank='7', suit='Clubs'),
            Card(rank='7', suit='Diamonds'),
            Card(rank='7', suit='Hearts')
        ]

        hand = Hand(cards=cards)
        assert hand.best_rank() == 'Four of a Kind'

    def test_hand_figures_out_straight_flush_is_best_rank(self):
        cards = [
            Card(rank=rank, suit='Diamonds')
            for rank in ['2', '3', '4', '5', '6']
        ]

        hand = Hand(cards=cards)
        assert hand.best_rank() == 'Straight Flush'

    def test_hand_figures_out_royal_flush_is_best_rank(self):
        cards = [
            Card(rank=rank, suit='Diamonds')
            for rank in ['10', 'Jack', 'Queen', 'King', 'Ace']
        ]

        hand = Hand(cards=cards)
        assert hand.best_rank() == 'Royal Flush'
