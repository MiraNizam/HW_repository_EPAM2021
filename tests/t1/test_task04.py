import pytest
from hw1.task04 import check_sum_of_four


def test_no_null_sum():
    """Testing that the def returns the right result if there is no any null sum"""
    assert check_sum_of_four([24, 1, 8], [15, 3, 8], [0, 6, 7], [6, 1, 7]) == 0


def test_all_null_sum():
    """Testing that the def returns the right result if all sum are null one"""
    assert check_sum_of_four([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]) == 256


@pytest.mark.parametrize(
    "a, b, c, d, result", [
        ([3, 1], [-3, 0], [2, -1], [-2, 0], 4),
        ([24, 1, 0], [15, 3, 0], [-20, 6, 7], [-4, -1, -7], 4),
        ([-5, 0, 0, -1], [-4, 0, -4, 5], [0, 7, 0, -4], [0, -3, 1, 8], 17)
    ]
)
def test_for_sum(a, b, c, d, result):
    assert check_sum_of_four(a, b, c, d) == result



