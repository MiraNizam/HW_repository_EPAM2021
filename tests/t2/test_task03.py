import pytest
from hw2.hw3 import combinations


def test_1_list():
    result = [[1], [3], [6], [8]]
    assert combinations([1, 3, 6, 8]) == result


def test_combinations_with_diff_len_elements():
    result = [
        [5, 'alpha', '1', 6],
        [5, 'omega', '1', 6],
        [5, 'beta', '1', 6],
        [6, 'alpha', '1', 6],
        [6, 'omega', '1', 6],
        [6, 'beta', '1', 6]
    ]
    assert combinations([5, 6], ["alpha", "omega", "beta"], "1", [6]) == result


def test_combinations_with_elements():
    result = [
        [1, 8, 1],
        [1, 8, 8],
        [1, 1, 1],
        [1, 1, 8],
        [8, 8, 1],
        [8, 8, 8],
        [8, 1, 1],
        [8, 1, 8]
    ]
    assert combinations([1, 8], [8, 1], [1, 8]) == result



