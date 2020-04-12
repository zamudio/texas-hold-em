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

    # def test_hand_figures_out_three_of_a_kind_is_best_rank(self):
    #     cards = [
    #         Card(rank='Ace', suit='Spades'),
    #         Card(rank='9', suit='Clubs'),
    #         Card(rank='7', suit='Diamonds'),
    #         Card(rank='Ace', suit='Diamonds'),
    #         Card(rank='7', suit='Hearts')
    #     ]

    #     hand = Hand(cards=cards)
    #     assert hand.best_rank() == 'Three of a kind'
