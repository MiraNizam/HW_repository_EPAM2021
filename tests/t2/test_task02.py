import pytest
from hw2.hw2 import major_and_minor_elem

@pytest.mark.parametrize(
    "array, max, min", [
        ([2, 2, 2, 5, 6, 5, 6, 6, 6, 6, 6], 6, 5),
        ([2, 2, 1, 1, 1, 2, 2], 2, 1),
        ([7, 1, 7], 7, 1)
    ]
)
def test_diff_elements(array, max, min):
    assert major_and_minor_elem(array) == (max, min)



