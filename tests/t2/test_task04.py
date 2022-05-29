from hw2.hw4 import cache


def test_cache():
    counter = 0

    @cache
    def func(a, b):
        nonlocal counter
        counter += 1
        return (a ** b) ** 2

    some = 10, 20

    val_1 = func(*some)
    val_2 = func(*some)

    assert val_1 is val_2
    assert counter == 1


def test_unhashable():
    counter = 0

    @cache
    def func(a):
        nonlocal counter
        counter += 1
        return a

    arg = "unhashable element"

    val_1 = func(arg)
    val_2 = func(arg)
    assert val_1 is val_2
    assert counter == 1


def test_cache_different_args():
    counter = 0

    @cache
    def func(a):
        nonlocal counter
        counter += 1
        return (a ** a) ** 2

    val_1 = func(4)
    val_2 = func(6)
    val_3 = func(8)
    val_4 = func(10)
    val_5 = func(15)

    assert counter == 5
    assert val_1 != val_2 and val_3 != val_4 and val_5 != val_1 and val_2 != val_4


