"""
A palindrome is a word that is the reverse of itself—that is, it is the same word when read forwards and backwards.

For example:

"madam" is a palindrome
"abba" is a palindrome
"cat" is not
"a" is a trivial case of a palindrome
"""


def is_palindrome(string):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    if len(string) <= 1:
        return True

    return is_palindrome(string[1:-1]) and (string[0] == string[-1])


if __name__ == '__main__':
    print("Pass" if (is_palindrome("")) else "Fail")
    print("Pass" if (is_palindrome("a")) else "Fail")
    print("Pass" if (is_palindrome("madam")) else "Fail")
    print("Pass" if (is_palindrome("abba")) else "Fail")
    print("Pass" if not (is_palindrome("Udacity")) else "Fail")
