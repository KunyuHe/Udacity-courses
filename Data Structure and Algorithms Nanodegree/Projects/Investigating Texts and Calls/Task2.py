"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from Task0 import csvToList


def go(calls):
    """
    TASK 2: Which telephone number spent the longest time on the phone
    during the period? Don't forget that time spent answering a call is
    also time spent on the phone.
    Print a message:
    "<telephone number> spent the longest time, <total time> seconds, on the phone during
    September 2016.".
    """
    number_time = {}

    for (self, other, _, length) in calls:
        number_time[self] = number_time.get(self, 0) + int(length)
        number_time[other] = number_time.get(other, 0) + int(length)

    number = max(number_time, key=number_time.get)
    return number, number_time[number]


if __name__ == '__main__':
    calls = csvToList('calls.csv')
    print(("{} spent the longest time, {} seconds, on the phone during "
           "September 2016.".format(*go(calls))))
