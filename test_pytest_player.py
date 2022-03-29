from player import Player
import pytest
from errors import ErrorSetPlayer


class TestPlayer:

    def setup(self):
        self.player = Player(0, 'Comp1')
        self.player2 = Player(1, 'User1')
        self.player2_2 = Player(1, 'User1')

    def test_equal(self):
        assert self.player2 == self.player2_2

    def test_init(self):
        assert self.player.type_player == 0
        assert self.player.name == 'Comp1'
        assert len(self.player._base_sample) == self.player._len_card
        assert isinstance(self.player._base_sample, set)

    def test_generate_card(self):
        self.player.generate_card()
        assert len(self.player._player_card) == self.player._h
        assert len([y for items in self.player._player_card for y in items if y.isdigit()]) == self.player._len_card

    def test_str(self):
        assert self.player.__str__() != ''
        assert self.player.name in self.player.__str__()
        # assert self.player.print(self.player.type_player) != ''
        # assert self.player.name in self.player.show_card(self.player.type_player)

    def test_set_list_players(self):
        assert Player.set_list_players(3, mode=['0', 'TEST']) == [Player(0, 'TEST'), Player(0, 'TEST'),
                                                                  Player(0, 'TEST')]
        with pytest.raises(ErrorSetPlayer):
            self.player.set_list_players(3, mode=['2', 'user_test'])

    def test_update_card(self):
        # checking computer
        # 1. check: if number not in card
        number = 100
        self.player.generate_card()
        assert self.player.update_card(number, self.player.type_player) == (1, 15, self.player.name)
        # 2. check: if number in card
        tmp_number_in_card = [int(y) for items in self.player._player_card for y in items if y.isdigit()][0]
        assert self.player.update_card(tmp_number_in_card, self.player.type_player) == (1, 14, self.player.name)
        # checking user
        # 3.1 check: if number not in card but user chose 'y'
        number = 100
        self.player2.generate_card()
        assert self.player2.update_card(number, self.player2.type_player,
                                        mode=True, auto_answer='y') == (0, 15, self.player2.name)
        # 3.2 check: if number not in card and user chose 'n'
        assert self.player2.update_card(number, self.player2.type_player,
                                        mode=True, auto_answer='n') == (1, 15, self.player2.name)
        # 3.3 check: if number in card and user chose 'y'
        tmp_number_in_card = [int(y) for items in self.player2._player_card for y in items if y.isdigit()][0]
        assert self.player2.update_card(tmp_number_in_card, self.player2.type_player,
                                        mode=True, auto_answer='y') == (1, 14, self.player2.name)
        # 3.4 check: if number in card but user chose 'n'
        tmp_number_in_card = [int(y) for items in self.player2._player_card for y in items if y.isdigit()][0]
        self.player2._len_card = 15  # hard reset counter card numbers
        assert self.player2.update_card(tmp_number_in_card, self.player2.type_player,
                                        mode=True, auto_answer='n') == (0, 15, self.player2.name)
