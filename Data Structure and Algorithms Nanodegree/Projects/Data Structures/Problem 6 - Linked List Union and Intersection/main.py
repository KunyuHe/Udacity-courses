from linked_lists import LinkedList


def union(llist_1, llist_2):
    llst = LinkedList()

    lst_1 = llist_1.to_list()
    lst_2 = llist_2.to_list()
    nodes = set(lst_1 + lst_2)

    for node in nodes:
        llst.append(node)

    return llst


def intersection(llist_1, llist_2):
    llst = LinkedList()

    lst_1 = llist_1.to_list()
    lst_2 = llist_2.to_list()
    nodes = set(lst_1).intersection(set(lst_2))

    for node in nodes:
        llst.append(node)

    return llst


if __name__ == '__main__':
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))

    # Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)
    for i in element_2:
        linked_list_4.append(i)
    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))
