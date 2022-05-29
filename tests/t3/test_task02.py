import time
import pytest

from hw3.task02.task02 import sum_slow_calc_500


@pytest.mark.skip
def test_sum_slow_calc_500():
    """The test checks the execution time of the function."""
    start_time = time.time()
    sum_slow_calc_500()
    finish_time = time.time()
    assert finish_time - start_time <= 60
