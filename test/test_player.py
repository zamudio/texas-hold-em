import pytest
from unittest.mock import MagicMock
from app.player import Player
from app.hand import Hand


class TestPlayer:
    def test_player_stores_name_and_cards(self):
        player_hand = Hand(cards=[])
        player = Player(name='M', hand=player_hand)
        assert player.name == 'M'
        assert player.hand == player_hand

    def test_player_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = 'Straight Flush'
        player = Player(name='M', hand=mock_hand)

        assert player.best_hand() == 'Straight Flush'
        assert mock_hand.best_rank.called
