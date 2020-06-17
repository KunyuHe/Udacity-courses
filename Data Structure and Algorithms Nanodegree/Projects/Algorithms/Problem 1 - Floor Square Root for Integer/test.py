from typing import Union

import pytest
from floored_sqrt import sqrt

CASES = [
    (0, 0),
    (1, 1),
    (9, 3),
    (16, 4),
    (27, 5),
    (16, 4),
    (-1, None),
    (9876543210123456789, 3142696805)
]


@pytest.mark.parametrize("input, expected", CASES)
def test_sqrt(input: int, expected: Union[int, None]):
    assert sqrt(input) == expected
