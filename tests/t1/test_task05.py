import pytest
from hw1.task05 import find_maximal_subarray_sum


def test_case_max_sum_k():
    """Testing if max sum is from k elements"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_case_max_sum_less_k():
    """Testing if max sum is from less k elements"""
    assert find_maximal_subarray_sum([-11, 3, 8, -3, 5, -8, 6, -1], 3) == 11


def test_case_empty_list():
    """Testing if the list is empty"""
    assert find_maximal_subarray_sum([], 3) is None


def test_case_all_nums_is_negative():
    """Testing if all nums < 0"""
    assert find_maximal_subarray_sum([-11, -13, -5, -1, -7, -3, -7, -6], 2) == -1