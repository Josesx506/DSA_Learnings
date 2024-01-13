"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

potential_telemarketers = set() # Set to hold unique numbers that place phone calls only
non_telemarketers = set()       # Set to hold every other number that does more than placing calls

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    # Telemarketers cannot send and recieve texts so all the numbers texting are non-telemarketers
    for text in texts:
        non_telemarketers.add(text[0]) # Text senders
        non_telemarketers.add(text[1]) # Text receivers

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    # Telemarketers can only place calls
    for call in calls:
        potential_telemarketers.add(call[0]) # Outgoing calls
        non_telemarketers.add(call[1])       # Incoming calls

# Subtract all non_tele numbers from outgoing
telemarketers = potential_telemarketers.difference(non_telemarketers)
# Sort the results and print line by line
telemarketers = "\n".join(sorted(telemarketers))

print(f"These numbers could be telemarketers: \n{telemarketers}")

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Possible telemarketers numbers are those which can only make outgoing calls but can't receive 
any incoming calls, send texts, and receive texts.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

