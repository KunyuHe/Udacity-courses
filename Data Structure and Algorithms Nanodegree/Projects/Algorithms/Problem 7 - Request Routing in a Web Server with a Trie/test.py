import pytest
from router import Router

ROUTER = Router("Home Page")
NOT_FOUND_HANDLER = "404 Page Not Found"
ROOT_HANDLER = "Home Page"
ABOUT_HANDLERS = ["About Page 0", "About Page 1", "About Page 2"]
NULL_HANDLER = "NULL Handler"

TEST_NORMAL = [
    (None, ("/", ROOT_HANDLER)),
    (("/home/about", ABOUT_HANDLERS[0]), ("/h", NOT_FOUND_HANDLER)),
    (None, ("/home", NOT_FOUND_HANDLER)),
    (None, ("/home/about", ABOUT_HANDLERS[0])),
    # Trailing "/" for searching, expected to return the first about handler
    ((None, ("/home/about/", ABOUT_HANDLERS[0]))),
    # Trailing "/" for inserting, expected to update the about handler
    (("/home/about/", ABOUT_HANDLERS[1]), ("/home/about", ABOUT_HANDLERS[1])),
    # Leading and two trailing "/"s for inserting, expected to update the about
    # handler
    (("//home/about//", ABOUT_HANDLERS[2]), ("/home/about", ABOUT_HANDLERS[2])),
    # Empty string for inserting and searching
    (("", NULL_HANDLER), ("", NOT_FOUND_HANDLER))
]

TEST_ERROR = [
    # Wrong input type for inserting
    ((123, NULL_HANDLER), None, TypeError),
    # Wrong input type for searching
    (None, 456, TypeError)
]


@pytest.mark.parametrize("insert, search", TEST_NORMAL)
def test_router(insert, search):
    if insert:
        ROUTER.add_handler(*insert)
    input, expected = search
    assert ROUTER.lookup(input) == expected


@pytest.mark.parametrize("insert, search, error", TEST_ERROR)
def test_router_error(insert, search, error):
    with pytest.raises(expected_exception=error):
        if insert:
            ROUTER.add_handler(*insert)
        if search:
            ROUTER.lookup(search)
