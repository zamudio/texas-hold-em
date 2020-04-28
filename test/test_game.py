import pytest
from unittest.mock import MagicMock, call
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

    def test_game_deals_two_initial_cards_from_deck_to_each_player(self):
        mock_deck = MagicMock()
        mock_players = [MagicMock(), MagicMock()]
        game = Game(
            deck=mock_deck,
            players=mock_players
        )

        game.play()
        mock_deck.remove_cards.assert_has_calls([
            call(2), call(2)
        ])

        # # safasf
        # mock_hand = []
        # for each_player in mock_players:
        #     cards = each_player.hand.cards
        #     for each_card in cards:
        #         mock_hand.append(each_card)

        # assert len(mock_hand) > 0
