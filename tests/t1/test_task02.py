from hw1.task02 import check_fibonacci


def test_positive_case():
    """Testing that fibonacci sequences give True"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21])


def test_negative_case():
    """Testing that not fibonacci sequences give False"""
    assert not check_fibonacci([0, 1, 1, 2, 3, 5, 8, 12, 21, 34])


def test_first_two_elements():
    """Testing that sequences of first two elements give correct result"""
    assert check_fibonacci([0, 1])


def test_positive_case_random_start():
    """Testing if a given sequence is part of a fibonacci sequence"""
    assert check_fibonacci([55, 89, 144, 233, 377, 610, 987])


def test_negative_random_start():
    """Testing if a given sequence is not part of a fibonacci sequence"""
    assert not check_fibonacci([13, 21, 34, 55, 89, 145, 233])
