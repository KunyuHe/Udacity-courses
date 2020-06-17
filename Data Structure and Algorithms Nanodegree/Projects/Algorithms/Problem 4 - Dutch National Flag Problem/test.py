import random

import pytest
from main import sort_012

TEST_NORMAL = [
    ([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]),
    ([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2,
      0, 0, 1]),
    ([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]),
    ([]),
    ([0, 0, 0, 0, 0]),
    ([0, 0, 1, 1]),
    ([random.choice((0, 1, 2)) for _ in range(99999)])
]

TEST_ERROR = [
    (['0', 1, 2],
     {
         'expected_exception': TypeError,
         'match': r"Elements in the input list should be integers."
     }),
    ([0, 1, 2, 3, 9],
     {
         'expected_exception': ValueError,
         'match': r"Elements in the input list should be 0, 1, or 2."
     })
]


@pytest.mark.parametrize("input", TEST_NORMAL)
def test_sort(input):
    assert sort_012(input) == sorted(input)


@pytest.mark.parametrize("input, error", TEST_ERROR)
def test_sqrt_error(input, error):
    with pytest.raises(**error):
        sort_012(input)
