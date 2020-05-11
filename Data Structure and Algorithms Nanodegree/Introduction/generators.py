def prod(a, b):
    # Change output to the product of a and b
    output = a * b
    return output


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # Update i and n
        i, n = i + 1, output


if __name__ == '__main__':
    my_gen = fact_gen()
    num = 5
    for i in range(num):
        print(next(my_gen))