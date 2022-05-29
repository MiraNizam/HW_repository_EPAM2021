"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Check that the given sequence is a Fibonacci sequence"""
    max_num = max(data)
    sequence = [0, 1]
    if data == sequence:
        return True

    while True:
        number = sequence[-1] + sequence[-2]
        if number <= max_num:
            sequence.append(number)
        else:
            break

    if min(data) not in sequence:
        return False
    min_num_idx = sequence.index(min(data))
    output = sequence[min_num_idx:]
    return output == data