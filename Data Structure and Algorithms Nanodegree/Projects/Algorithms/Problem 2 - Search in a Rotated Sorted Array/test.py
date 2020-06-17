import pytest
from rotated_array_search import search


def search_benchmark(arr, num):
    try:
        return arr.index(num)
    except ValueError:
        return -1


CASES = [
    ([6, 7, 8, 9, 10, 1, 2, 3, 4], 6),
    ([6, 7, 8, 9, 10, 1, 2, 3, 4], 1),
    ([6, 7, 8, 1, 2, 3, 4], 8),
    ([6, 7, 8, 1, 2, 3, 4], 1),
    ([6, 7, 8, 1, 2, 3, 4], 10),
    ([], 123),
    (list(range(10 ** 5)), 10)
]


@pytest.mark.parametrize("arr, number", CASES)
def test_search(arr, number):
    assert search(arr, number) == search_benchmark(arr, number)
