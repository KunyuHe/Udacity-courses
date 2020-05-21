import pytest
from group import create_mad_men_tree
from main import is_user_in_group

parent, child, sub_child = create_mad_men_tree()

TEST_CASES = [
    ('Kevin', sub_child, True),
    ('Joan', child, True),
    ('Sally', parent, True),
    ('Don', sub_child, False),
    ('Archie', parent, True),
    ('Betty', parent, True),
    ('', parent, False),
    ('  ', child, False)
]


@pytest.mark.parametrize("user,group,expected", TEST_CASES)
def test_is_user_in_group(user, group, expected):
    assert is_user_in_group(user, group) == expected


if __name__ == '__main__':
    pytest.main()
