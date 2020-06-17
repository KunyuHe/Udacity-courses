from typing import Union

import pytest
from floored_sqrt import sqrt

TEST_NORMAL = [
    (0, 0),
    (1, 1),
    (9, 3),
    (16, 4),
    (27, 5),
    (9876543210123456789, 3142696805)
]

TEST_ERROR = [
    (-1,
     {
         'expected_exception': ValueError,
         'match': r'Input should be non-negative.'
     }),
    (1.1,
     {
         'expected_exception': TypeError,
         'match': r'Input should be an integer.'
     })
]


@pytest.mark.parametrize("input, expected", TEST_NORMAL)
def test_sqrt(input: int, expected: Union[int, None]):
    assert sqrt(input) == expected


@pytest.mark.parametrize("input, error", TEST_ERROR)
def test_sqrt_error(input, error):
    with pytest.raises(**error):
        sqrt(input)
