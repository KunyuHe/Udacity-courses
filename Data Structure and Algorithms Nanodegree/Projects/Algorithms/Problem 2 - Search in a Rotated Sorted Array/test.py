import pytest
from rotated_array_search import search


def search_benchmark(arr, num):
    try:
        return arr.index(num)
    except ValueError:
        return -1


TEST_NORMAL = [
    ([6, 7, 8, 9, 10, 1, 2, 3, 4], 6),
    ([6, 7, 8, 9, 10, 1, 2, 3, 4], 1),
    ([6, 7, 8, 1, 2, 3, 4], 8),
    ([6, 7, 8, 1, 2, 3, 4], 1),
    ([6, 7, 8, 1, 2, 3, 4], 10),
    ([], 123)
]

TEST_ERROR = [
    (['cat', 2, 4, 100], 2),
    ([1, 2, 3], '1')
]


@pytest.mark.parametrize("arr, number", TEST_NORMAL)
def test_search(arr, number):
    assert search(arr, number) == search_benchmark(arr, number)


@pytest.mark.parametrize("arr, number", TEST_ERROR)
def test_search_error(arr, number):
    with pytest.raises(expected_exception=TypeError):
        search(arr, number)
