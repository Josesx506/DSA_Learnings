"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

all_numbers = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for row in texts:
        all_numbers.append(row[0])
        all_numbers.append(row[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for row in calls:
        all_numbers.append(row[0])
        all_numbers.append(row[1])

print(f"There are {len(set(all_numbers))} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
