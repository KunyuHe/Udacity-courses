import pytest
from main import rearrange_digits

CASES = [
    ([1, 2, 3, 4, 5], [(531, 42)]),
    ([4, 6, 2, 5, 9, 8], [(964, 852)]),
    ([], [None]),
    ([1], [None]),
    ([1, 0], [(1, 0)]),
    ([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [(999999, 99999)])
]


@pytest.mark.parametrize("input, expected", CASES)
def test_rearrange_digits(input, expected):
    assert rearrange_digits(input) in expected
