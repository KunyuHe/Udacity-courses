"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

from Task0 import csvToList


def getTelemarketers(texts, calls):
    outcalls, incalls = [], []
    outtexts, intexts = [], []

    for text in texts:
        outtexts.append(text[0])
        intexts.append(text[1])

    for call in calls:
        outcalls.append(call[0])
        incalls.append(call[1])

    res = list(set(outcalls) - set(incalls) - set(outtexts) - set(intexts))
    return res


if __name__ == '__main__':
    texts = csvToList('texts.csv')
    calls = csvToList('calls.csv')

    telemarketers = getTelemarketers(texts, calls)
    print("These numbers could be telemarketers: ")
    print("\n".join(sorted(telemarketers)))
