from app.main import find_max
import pytest


def test_positive_numbers():
    assert find_max([1, 2, 3]) == 3


def test_negative_numbers():
    assert find_max([-1, -5, -2]) == -1


def test_single_element():
    assert find_max([10]) == 10


def test_empty_list():
    with pytest.raises(ValueError):
        find_max([])
