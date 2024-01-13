"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    all_texters = []

    for row in texts:
        all_texters.append(row[0])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    all_callers = []

    for row in calls:
        all_callers.append(row[0])

unique_texters = list(set(all_texters))
unique_callers = list(set(all_callers))

telemarketers = []

for idx,num in enumerate(unique_callers):
    if num not in unique_texters:
        telemarketers.append(num)

telemarketers = "\n".join(sorted(telemarketers))

print(f"These numbers could be telemarketers: \n{telemarketers}")

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

