import string
from hw2.hw5 import custom_range


def test_with_one_arg():
    """ The function received Iterable and one arg that must work as STOP in slicing"""
    result = ['a', 'b', 'c', 'd', 'e', 'f']
    assert custom_range(string.ascii_lowercase, 'g') == result


def test_with_two_args():
    """ The function received Iterable and two args that must work as START and STOP in slicing"""
    result = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert custom_range(string.ascii_lowercase, 'g', 'p') == result


def test_with_three_args():
    """ The function received Iterable and three args that must work as START, STOP and STEP in slicing"""
    result = ['p', 'n', 'l', 'j', 'h']
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == result

