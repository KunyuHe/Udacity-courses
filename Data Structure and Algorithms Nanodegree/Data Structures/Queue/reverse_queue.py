from linked_list_queue import Queue


def reverse_queue(queue):
    """
    Reverese the input queue

    Args:
       queue(queue): Queue to be reversed
    Returns:
       queue: Reveresed queue
    """
    holder = Queue()

    while not queue.is_empty():
        holder.enqueue(queue.dequeue())

    queue = None
    return holder


def test_function(test_case):
    queue = Queue()
    for num in test_case:
        queue.enqueue(num)

    reverse_queue(queue)
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")


if __name__ == '__main__':
    test_case_1 = [1, 2, 3, 4]
    test_function(test_case_1)

    test_case_2 = [1]
    test_function(test_case_2)
