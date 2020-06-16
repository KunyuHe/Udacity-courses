def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    start_ind, end_ind = 0, len(array) - 1

    while end_ind > start_ind:
        ind = (start_ind + end_ind) // 2
        if array[ind] == target:
            return ind
        elif array[ind] > target:
            end_ind = ind - 1
        else:
            start_ind = ind + 1
    else:
        return None


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    index = 6
    test_case = [array, target, index]
    test_function(test_case)