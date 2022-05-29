from hw3.task04.task04 import is_armstrong


def test_is_armstrong():
    """
    Test checks that func return True if it is Armstrong number
    """
    assert is_armstrong(153)
    assert is_armstrong(9474)


def test_is_not_armstrong():
    """
    Test checks that func return false if it is not Armstrong number
    """
    assert not is_armstrong(10)
    assert not is_armstrong(15600)


def test_works_with_null():
    """
    Test return True if we give 0
    """
    assert is_armstrong(0) is True
