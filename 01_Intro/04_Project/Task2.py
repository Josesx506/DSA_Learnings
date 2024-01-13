"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
    # Old implementation that only get the 
    # top_number,duration = None,None
    # for rows in calls:
    #     call_dur = int(rows[3])
    #     if duration == None or call_dur>=duration:
    #         duration = call_dur
    #         top_number = rows[1]
    
    phone_dict={}
    for call in calls:
        # Extract the minutes of the calls placed
        phone_dict[call[0]] = phone_dict.get(call[0], 0) + int(call[3])

        # Extract the minutes of the calls received
        phone_dict[call[1]] = phone_dict.get(call[1], 0) + int(call[3])
    
    duration, top_number = max(zip(phone_dict.values(), phone_dict.keys()))#[0,1]

print(f"{top_number} spent the longest time, {duration} seconds, on the phone during September 2016.")

# import json
# print(json.dumps(phone_dict, indent=4, sort_keys=True, default=str))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.

We have to find the phone number which spent the longest time on the phone (calling and receiving) and 
also the total time spent instead you have only considered the time spent.

Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

