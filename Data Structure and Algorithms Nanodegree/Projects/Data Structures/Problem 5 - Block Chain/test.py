import pytest
from blockchain import create_mad_men_blockchain

TEST_SEARCH = [
    ('Midge', True),
    ('Peggy', False),
    ('Joan', False),
    ('Megan', True),
    ('Betty', True),
    ('Sally', False),
    ('Bethany', False)
]


def test_size():
    madmen = create_mad_men_blockchain()
    assert madmen.size() == 7


@pytest.mark.parametrize('data,expected', TEST_SEARCH)
def test_search(data, expected):
    madmen = create_mad_men_blockchain()
    assert (madmen.search(data) is not None) == expected


if __name__ == '__main__':
    pytest.main()
