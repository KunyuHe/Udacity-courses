import random

import pytest
from main import get_min_max

TEST_NORMAL = [
    ([i for i in range(0, 10)]),
    ([]),
    ([1, 1, 1, 1, 1, 1, 1]),
    ([-1, -5, 10, 10, -5])
]

TEST_ERROR = [
    (["1", 1, 1, 2],
     {
         'expected_exception': TypeError,
         'match': r"Input list should be an array of integers."
     })
]


@pytest.mark.parametrize("input", TEST_NORMAL)
def test_get_minmax(input):
    if not input:
        assert get_min_max(input) is None
    else:
        random.shuffle(input)
        assert get_min_max(input) == (min(input), max(input))


@pytest.mark.parametrize("input, error", TEST_ERROR)
def test_suffixes_error(input, error):
    with pytest.raises(**error):
        get_min_max(input)
