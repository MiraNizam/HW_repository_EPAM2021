"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


from typing import Iterable, List


def custom_range(values: Iterable, *position) -> List[List]:
    """The function accepts iterable values and [start:stop:step] it behaves as range function"""

    if not position or len(position) > 3:
        raise ValueError("Invalid arguments. The def should has from 1 to 3 arguments [start:stop:step]")

    start = values.index(position[0]) if len(position) > 1 else 0
    stop = (
        values.index(position[0])
        if len(position) == 1
        else values.index(position[1])
    )
    step = position[2] if len(position) == 3 else 1

    return list(values[start:stop:step])
