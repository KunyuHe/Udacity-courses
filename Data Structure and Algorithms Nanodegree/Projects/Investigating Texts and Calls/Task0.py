"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def csvToList(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)


def go(texts, calls):
    """
    TASK 0:
    What is the first record of texts and what is the last record of calls?
    Print messages:
    "First record of texts, <incoming number> texts <answering number> at time <time>"
    "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
    """
    print("First record of texts, {} texts {} at time {}".format(*texts[0]))
    print(
        "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
            *calls[-1]))


if __name__ == '__main__':
    texts = csvToList('texts.csv')
    calls = csvToList('calls.csv')

    go(texts, calls)
