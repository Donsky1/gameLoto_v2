import unittest
from functions import *
from loto import Loto


class TestLoto(unittest.TestCase):

    def test_play_2computers(self):
        # get winners
        player_list = set_players(2, computer=True, pair=True)
        game = Loto(2, player_list)
        self.assertEqual(game.play(show_card=True), 1)

    def test_play_2users(self):
        # get losers
        player_list = set_players(2, computer=False, pair=True)
        game = Loto(2, player_list)
        self.assertEqual(game.play(show_card=True, mode=True), 0)
        self.assertFalse(game.play(show_card=True, mode=True))