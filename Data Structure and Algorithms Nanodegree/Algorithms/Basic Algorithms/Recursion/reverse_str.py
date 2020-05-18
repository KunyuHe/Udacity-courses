def reverse_string(string):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """
    if len(string) == 0:
        return ""

    return reverse_string(string[1:]) + string[0]

if __name__ == '__main__':
    print("Pass" if ("" == reverse_string("")) else "Fail")
    print("Pass" if ("cba" == reverse_string("abc")) else "Fail")