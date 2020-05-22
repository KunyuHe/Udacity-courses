def towerofHanoi(num_disks, source="S", auxiliary="A", destination="D"):
    if num_disks == 0:
        return None

    if num_disks == 1:
        print("{} {}".format(source, destination))
        return None

    # Move (n-1) to auxiliary
    towerofHanoi(num_disks - 1, source, destination, auxiliary)
    # Move the largest one to destination
    print("{} {}".format(source, destination))
    # Move (n-1) from auxiliary to destination
    towerofHanoi(num_disks - 1, auxiliary, source, destination)


if __name__ == '__main__':
    towerofHanoi(2)
    print("\n\n")

    towerofHanoi(3)
    print("\n\n")

    towerofHanoi(4)
    print("\n\n")
