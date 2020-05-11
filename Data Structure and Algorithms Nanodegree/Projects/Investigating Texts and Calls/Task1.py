"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from Task0 import csvToList


def go(texts, calls):
    """
    TASK 1:
    How many different telephone numbers are there in the records?
    Print a message:
    "There are <count> different telephone numbers in the records."
    """
    nums = []

    for text in texts:
        nums += text[:2]
    for call in calls:
        nums += call[:2]

    return len(set(nums))


if __name__ == '__main__':
    texts = csvToList('texts.csv')
    calls = csvToList('calls.csv')

    print("There are %i different telephone numbers in the records." % go(texts,
                                                                          calls))
