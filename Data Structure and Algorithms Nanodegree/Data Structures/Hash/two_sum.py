def twoSum(arr, target):
    value_index = {}

    for i, num in enumerate(arr):
        lookup = target - num
        if lookup in value_index:
            return value_index[lookup], i
        value_index[num] = i

    return None


def test_function(test_case):
    output = twoSum(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
    test_function(test_case_1)

    test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
    test_function(test_case_2)

    test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
    test_function(test_case_3)
