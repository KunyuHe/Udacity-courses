import pytest
from main import go

TEST_EQUAL = [
    "aaaaaaaaaaaaaa",
    "AAAAAAABBBCCCCCCCDDEEEEEE",
    "DBDBDBDBDBDBDBDBDBDBDBDBDB",
    "         ---***121243adbasdbaSAJDBASIDJAp8506846"
]

TEST_ENCODING = [
    ("aaaaaaaaaaaaaa", "00000000000000"),
    ("AAAAAAABBBCCCCCCCDDEEEEEE",
     "1010101010101000100100111111111111111000000010101010101"),
    ("DBDBDBDBDBDBDBDBDBDBDBDBDB", "01010101010101010101010101")
]


@pytest.mark.parametrize("text", TEST_EQUAL)
def test_loss(text):
    _, decoded_text = go(text)
    assert decoded_text == text


@pytest.mark.parametrize("text,expected_encoded", TEST_ENCODING)
def test_encoding(text, expected_encoded):
    encoded_text, _ = go(text)
    assert encoded_text == expected_encoded


def test_empty():
    with pytest.raises(ValueError, match="Text is empty. Abort encoding."):
        go("")


if __name__ == '__main__':
    pytest.main()
