import unittest
from player import Player
from loto import Loto


class TestLoto(unittest.TestCase):

    def test_play_2computers(self):
        # get winners
        player_list = Player.set_players(2, computer=True, pair=True)
        game = Loto(2, player_list)
        self.assertEqual(game.play(show_card=False), 1)

    def test_play_2users(self):
        # get losers
        player_list = Player.set_players(2, computer=False, pair=True)
        game = Loto(2, player_list)
        self.assertEqual(game.play(show_card=False, mode=True), 0)
        self.assertFalse(game.play(show_card=False, mode=True))

    def test_set_player(self):
        self.assertEqual(len(Player.set_players(2, computer=False, pair=True)), 2)
