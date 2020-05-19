def stairCase(n):
    n_cnt = {1: 1,
             2: 2,
             3: 4}

    def climb(n):
        if n in n_cnt:
            return n_cnt[n]
        cnt = climb(n - 1) + climb(n - 2) + climb(n - 3)
        n_cnt[n] = cnt
        return cnt

    return climb(n)


def test_function(test_case):
    answer = stairCase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_case = [4, 7]
    test_function(test_case)

    test_case = [5, 13]
    test_function(test_case)

    test_case = [3, 4]
    test_function(test_case)

    test_case = [20, 121415]
    test_function(test_case)
