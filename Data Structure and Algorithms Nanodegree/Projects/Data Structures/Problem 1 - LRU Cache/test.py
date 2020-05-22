import pytest

from LRU_Cache import LRU_Cache

TEST_NORMAL = [
    ((5, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], 1),
     -1),

    ((3, [("Jan", 1), ("Feb", 2), ("Mar", 3), ("Apr", 4)], "Mar"),
     3)
]

TEST_ERROR = [
    (('capacity', [], 1),
     {'expected_exception': TypeError,
      'match': "Cache capacity is of type.*. It must be an integer."}),

    ((0, [], 1),
     {'expected_exception': ValueError,
      'match': "Cache capacity must be a positive integer."}),

    ((5, [(1, 1), (2, 2), (None, 3)], 1),
     {'expected_exception': ValueError,
      'match': "Set key is missing."}),

    ((5, [([1, 2], 1), (2, 2), (3, 3)], 3),
     {'expected_exception': TypeError,
      'match': r'Key is of type.*. It is not hashable.'}),

    ((5, [(1, 1), (2, 2), (3, 3)], None),
     {'expected_exception': KeyError,
      'match': "Search key is missing."})
]


def create_cache(capacity, lst):
    cache = LRU_Cache(capacity)

    for key, value in lst:
        cache.set(key, value)

    return cache


@pytest.mark.parametrize("input, expected_output", TEST_NORMAL)
def test_normal(input, expected_output):
    capacity, lst, key = input
    cache = create_cache(capacity, lst)
    assert cache.get(key) == expected_output


@pytest.mark.parametrize("input, error", TEST_ERROR)
def test_error(input, error):
    capacity, lst, key = input
    with pytest.raises(**error):
        cache = create_cache(capacity, lst)
        cache.get(key)


def test_cache_update():
    capacity, lst = 5, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    cache = create_cache(capacity, lst)

    cache.get(1)
    cache.set(6, 6)
    assert cache.get(6) == 6
    assert cache.get(1) == 1
    assert cache.get(2) == -1


if __name__ == '__main__':
    pytest.main()
