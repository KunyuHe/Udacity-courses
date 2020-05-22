import pytest
from linked_lists import LinkedList
from main import union, intersection

BASE = [
    ([3, 2, 4, 35, 6, 65, 6, 4, 3, 21],
     [6, 32, 4, 9, 6, 1, 11, 21, 1]),
    ([3, 2, 4, 35, 6, 65, 6, 4, 3, 23],
     [1, 7, 8, 9, 11, 21, 1]),
    ([22, 7, 4, 35, 6, 65, 6, 4, 3, 23],
     [1, 7, 8, 65, 11, 21, 1]),
    ([],
     [1, 7, 8]),
    ([],
     [])
]

UNION = [
    "32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->",
    "65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->",
    "65 -> 1 -> 35 -> 4 -> 3 -> 6 -> 7 -> 8 -> 11 -> 21 -> 22 -> 23 ->",
    "8 -> 1 -> 7",
    ""
]

TEST_UNION = list(zip(BASE, UNION))

INTERSECTION = [
    "4 -> 21 -> 6 -> ",
    "",
    "65 -> 7 -> ",
    "",
    ""
]

TEST_INTERSECTION = list(zip(BASE, INTERSECTION))


def get_llst(lst1, lst2):
    llst1 = LinkedList()
    llst2 = LinkedList()
    for value in lst1:
        llst1.append(value)
    for value in lst2:
        llst2.append(value)
    return llst1, llst2


@pytest.mark.parametrize("input, expected", TEST_UNION)
def test_union(input, expected):
    lst1, lst2 = input
    llst1, llst2 = get_llst(lst1, lst2)

    assert str(union(llst1, llst2)) == expected


@pytest.mark.parametrize("input, expected", TEST_INTERSECTION)
def test_union(input, expected):
    lst1, lst2 = input
    llst1, llst2 = get_llst(lst1, lst2)

    assert str(intersection(llst1, llst2)) == expected


if __name__ == '__main__':
    pytest.main()
