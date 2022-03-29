import pytest
from main import play_game_mode
from errors import ErrorCountPlayers, ErrorChoice


def test_main_non_error():
    with pytest.raises(ErrorChoice):
        play_game_mode('10')


def test_main_3():
    assert play_game_mode('3') == 1


def test_main_4_error():
    with pytest.raises(ErrorCountPlayers):
        play_game_mode('4', 'abc')



