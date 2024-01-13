"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def code_extractor(phone):
    '''Function to extract the phone code depending on the device type'''
    mobile = phone.split(' ')

    if phone.startswith("(0"):
        code = phone.split(')')[0].replace('(','')
    elif len(mobile) == 2 and (mobile[0].startswith("7") or mobile[0].startswith("8") or mobile[0].startswith("9")):
        code = mobile[0][:4]
    elif phone.startswith("(140)"):
        code = "(140)"
    
    return code

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    banglore_codes = []

    for row in calls:
      caller_id = row[0]  
      if caller_id.startswith("(080)"):
          code = code_extractor(row[1])
          banglore_codes.append(code)

    
# Part A:
unique_codes = "\n".join(sorted(set(banglore_codes)))

print(f"The numbers called by people in Bangalore have codes:\n{unique_codes}")

print('\n\n\n')
  

# Part B:
counter = 0
for code in banglore_codes:
    if code == '080':
        counter += 1

percent = (counter/len(banglore_codes)) * 100

print(f"{percent: .2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
