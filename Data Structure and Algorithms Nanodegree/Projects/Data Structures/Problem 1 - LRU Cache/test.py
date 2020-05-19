import pytest

from LRU_Cache import LRU_Cache


def create_cache():
    cache = LRU_Cache(5)

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)

    return cache


def test_get():
    cache = create_cache()

    assert cache.get(9) == -1

    assert cache.get(1) == 1

    with pytest.raises(ValueError, match='Key is missing.'):
        cache.get(None)

    cache.set(5, 5)
    cache.set(6, 6)
    assert cache.get(1) == 1
    assert cache.get(2) == -1


def test_set():
    cache = create_cache()

    cache.set(5, 5)
    assert cache.get(5) == 5

    cache.set("June", 6)
    assert cache.get("June") == 6

    cache.set((1), "January Tuple")
    assert cache.get((1)) == "January Tuple"

    with pytest.raises(ValueError, match='Key is missing.'):
        cache.set(None, 1)

    with pytest.raises(TypeError,
                       match=r'Key is of type.*. It is not hashable.'):
        cache.set([2], 2)


if __name__ == '__main__':
    pytest.main()
