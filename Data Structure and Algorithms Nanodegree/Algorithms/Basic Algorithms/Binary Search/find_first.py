from recursive import binary_search_recursive


def find_first(array, target):
    ind = binary_search_recursive(array, target)
    if not ind:
        return None

    while array[ind - 1] == target and ind > 0:
        ind -= 1

    return ind


if __name__ == '__main__':
    multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
    print(find_first(multiple, 7))  # Should return 3
    print(find_first(multiple, 9))  # Should return None