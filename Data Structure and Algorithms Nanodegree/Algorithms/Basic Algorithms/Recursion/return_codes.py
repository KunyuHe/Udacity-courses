"""
Problem statement
In an encryption system where ASCII lower case letters represent numbers in the
pattern a=1, b=2, c=3... and so on, find out all the codes that are possible
for a given input number.

Example 1

number = 123
codes_possible = ["aw", "abc", "lc"]
Explanation: The codes are for the following number:

1 . 23 = "aw"
1 . 2 . 3 = "abc"
12 . 3 = "lc"
Example 2

number = 145
codes_possible = ["ade", "ne"]
Return the codes in a list. The order of codes in the list is not important.

Note: you can assume that the input number will not contain any 0s
"""


def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember:
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    return chr(number + 96)


def all_codes(number):
    if number == 0:
        return [""]

    # Calculate for the two right-most digits
    last_two = number % 100
    res_last_two = list()
    if last_two <= 26 and number > 9:
        res_last_two = all_codes(number // 100)
        alphabet = get_alphabet(last_two)
        res_last_two = [x + alphabet for x in res_last_two]

    # Calculate for the right-most digit
    last_one = number % 10
    res_last_one = all_codes(number // 10)
    alphabet = get_alphabet(last_one)
    res_last_one = [x + alphabet for x in res_last_one]

    return res_last_two + res_last_one


def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]

    output = all_codes(number)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    number = 123
    solution = ['abc', 'aw', 'lc']
    test_case = [number, solution]
    test_function(test_case)

    number = 145
    solution = ['ade', 'ne']
    test_case = [number, solution]
    test_function(test_case)

    number = 1145
    solution = ['aade', 'ane', 'kde']
    test_case = [number, solution]
    test_function(test_case)

    number = 4545
    solution = ['dede']
    test_case = [number, solution]
    test_function(test_case)
