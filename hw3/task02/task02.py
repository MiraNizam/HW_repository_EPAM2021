"""Here's a not very efficient calculation function that calculates something important::
...
Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function."""

import time
import struct
import random
import hashlib
from multiprocessing import Pool

def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return print(sum(struct.unpack('<' + 'B' * len(data), data)))

def sum_slow_calc_500():
    """The function calculates total sum of slow_calculate() of all numbers starting from 0 to 500"""
    with Pool(500) as p:
        return sum(p.map(slow_calculate, range(501)))
