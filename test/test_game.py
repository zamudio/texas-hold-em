import pytest
from unittest.mock import MagicMock
from app.game import Game


class TestGame:
    def test_game_stores_deck_and_players(self):
        mock_deck = MagicMock()
        mock_players = [MagicMock(), MagicMock()]
        game = Game(
            deck=mock_deck,
            players=mock_players
        )

        assert game.deck == mock_deck
        assert game.players == mock_players

    def test_game_shuffles_deck_on_play(self):
        mock_deck = MagicMock()
        mock_players = [MagicMock(), MagicMock()]
        game = Game(
            deck=mock_deck,
            players=mock_players
        )

        game.play()
        assert mock_deck.shuffle.called
