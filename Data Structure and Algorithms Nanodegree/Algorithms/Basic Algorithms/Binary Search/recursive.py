def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    def _search(start_index, end_index):
        if end_index <= start_index:
            return None

        ind = (start_index + end_index) // 2
        if array[ind] == target:
            return ind
        elif array[ind] > target:
            return _search(start_index, ind - 1)
        else:
            return _search(ind + 1, end_index)

    return _search(0, len(array) - 1)

def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 4
    index = 4
    test_case = [array, target, index]
    test_function(test_case)
