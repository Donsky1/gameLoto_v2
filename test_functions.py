from functions import *
import pytest


def test_set_list_players():
    with pytest.raises(Exception):
        set_list_players('asd')
    assert len(set_list_players(5, mode=True)) == 5
    for p in set_list_players(15, mode=True):
        assert p is not None


def test_set_players():
    assert len(set_players(2, computer=True, pair=True)) == 2
    assert len(set_players(2, computer=False, pair=True)) == 2
    assert len(set_players(2, computer=True, pair=False)) == 2
    for p in set_players(5, computer=True, pair=True, mode=True):
        assert p is not None
