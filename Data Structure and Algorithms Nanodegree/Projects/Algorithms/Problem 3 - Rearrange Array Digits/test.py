import pytest
from main import rearrange_digits

TEST_NORMAL = [
    ([1, 2, 3, 4, 5], [(531, 42)]),
    ([4, 6, 2, 5, 9, 8], [(964, 852)]),
    ([1, 0], [(1, 0)]),
    ([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [(999999, 99999)])
]

TEST_ERROR = [
    ([1],
     {
         'expected_exception': ValueError,
         'match': r"Input list should have more than one digit for partition."
     }),
    ([1, '2', 3, 4],
     {
         'expected_exception': TypeError,
         'match': r"Elements in the input list should be integers."
     }),
    ([1, 23, 4],
     {
         'expected_exception': ValueError,
         'match': r"Elements in the input list should be digits."
     })
]


@pytest.mark.parametrize("input, expected", TEST_NORMAL)
def test_rearrange_digits(input, expected):
    assert rearrange_digits(input) in expected


@pytest.mark.parametrize("input, error", TEST_ERROR)
def test_rearrange_error(input, error):
    with pytest.raises(**error):
        rearrange_digits(input)
