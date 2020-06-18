import pytest
from trie import Trie

WORDS = ["ant", "anthology", "antagonist", "antonym",
         "fun", "function", "factory",
         "trie", "trigger", "trigonometry", "tripod"]

TRIE = Trie()
for word in WORDS:
    TRIE.insert(word)

TEST_NORMAL = [
    ("ant", ['hology', 'agonist', 'onym']),
    ("f", ['un', 'unction', 'actory']),
    ("trig", ['ger', 'onometry']),
    ("z", None),
    ("trigonometry", [])
]

TEST_ERROR = [
    (1,
     {
         'expected_exception': TypeError,
         'match': r"Prefix must be string."
     }),
    ("",
     {
         'expected_exception': ValueError,
         'match': r"Prefix cannot be an empty string."
     })
]


@pytest.mark.parametrize("input, expected", TEST_NORMAL)
def test_suffixes(input, expected):
    assert TRIE.suffixes(input) == expected


@pytest.mark.parametrize("input, error", TEST_ERROR)
def test_suffixes_error(input, error):
    with pytest.raises(**error):
        TRIE.suffixes(input)