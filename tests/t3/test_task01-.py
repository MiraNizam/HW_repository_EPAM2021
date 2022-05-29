from unittest.mock import Mock, call
from hw3.task01.task01 import cache_deco


def test_not_cached_with_diff_arguments():
    mock = Mock()
    cached_function = cache_deco(times=1)(mock)
    cached_function(1, 3)
    cached_function(3, 1)
    cached_function(1, 3)
    cached_function(3, 1)
    cached_function(1, 3)
    cached_function(3, 1)
    assert mock.mock_calls == [call(1, 3), call(3, 1), call(1, 3), call(3, 1)]


def test_cached_with_same_argument():
    mock = Mock()
    cached_function = cache_deco(times=1)(mock)
    cached_function(1, 3)
    cached_function(1, 3)
    cached_function(1, 3)
    assert mock.mock_calls == [call(1, 3), call(1, 3)]