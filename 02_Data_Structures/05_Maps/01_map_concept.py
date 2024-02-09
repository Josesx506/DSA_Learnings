'''
Python Dictionary - Introduction

In Python, the map concept appears as a built-in data type called a dictionary. A dictionary contains key-value pairs. 
Dictionaries might soon become your favorite data structure in Python—they're extremely easy to use and useful. Here's 
a sample of setting up a dictionary.
'''

udacity = {}
udacity['u'] = 1
udacity['d'] = 2
udacity['a'] = 3
udacity['c'] = 4
udacity['i'] = 5
udacity['t'] = 6
udacity['y'] = 7

print (udacity)
# {'u': 1, 'd': 2, 'a': 3, 'c': 4, 'i': 5, 't': 6, 'y': 7}

'''
In this case, the letters in "udacity" were each keys in our dictionary, and the position of that letter in the string 
was the value. Thus, I can do the following:
'''
print (udacity['t'])
# 6

'''
This statement is saying "go to the key labeled 't' and find it's value, 6".

Dictionaries are wonderfully flexible—you can store a wide variety of structures as values. You store another 
dictionary or a list:
'''
dictionary = {}
dictionary['d'] = [1]
dictionary['i'] = [2]
dictionary['c'] = [3]
dictionary['t'] = [4]
dictionary['i'].append(5)
dictionary['o'] = [6]
dictionary['n'] = [7]
dictionary['a'] = [8]
dictionary['r'] = [9]
dictionary['y'] = [10]
print (dictionary)
# {'d': [1], 'i': [2, 5], 'c': [3], 't': [4], 'o': [6], 'n': [7], 'a': [8], 'r': [9], 'y':[10]}

'''
Exercise
Time to play with Python dictionaries! You're going to work on a dictionary that stores cities by country and 
continent. The following one is done for you - the city of Mountain View is in the USA, which is in North America.

locations = {'North America': {'USA': ['Mountain View']}}

Notice that:
    - locations is a dictionary of dictionaries
    - North America (Continent) is a dictionary
    - USA (Country) is a key
    - ['Mountain View'] (City) is a list acting as a value. A new city within USA country can be "appended" to the given list.

Task 1
You need to add the cities listed below by modifying the given structure. Cities to add:
    - Bangalore (India, Asia)
    - New Delhi (India, Asia)
    - Atlanta (USA, North America)
    - Cairo (Egypt, Africa)
    - Shanghai (China, Asia)

Be careful, while adding a city in an existing country. Consider adding it to the existing list of cities as:
    - locations['Asia']['India'].append('New Delhi')

Task 2
Print the following (using "print") by looking them up in the structure.

1. A list of all cities in the USA in alphabetic order.
2. All cities in Asia, in alphabetic order, next to the name of the country. In your output, label each answer 
with a number so it looks like this:
    1
    American City
    American City
    2
    Asian City - Country
    Asian City - Country
'''
# My Code
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Banglore']}
locations['Asia']['India'].append('New Delhi')
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Eygpt': ['Cairo']}


# TODO: Print a list of all cities in the USA in alphabetic order.

# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country
am_c = locations['North America'].keys()
as_c = locations['Asia'].keys()

all_c = [am_c,as_c]

for idx,co_lt in enumerate(all_c):
    if idx == 0:
        print(idx+1)
        for co in co_lt:
            for k,v in enumerate(sorted(locations['North America'][co])):
                print(v)
    else:
        print(idx+1)
        for co in co_lt:
            for k,v in enumerate(sorted(locations['Asia'][co])):
                print(f"{v} - {co}")


# Udacity Solution
# Task 1 - Solution
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['India'].append('New Delhi')
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

# Task 2 - Solution
# Part 1 - A list of all cities in the USA in alphabetic order.
print (1)
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print (city)

# Part 2 - All cities in Asia, in alphabetic order
print (2)
asia_cities = []
for country, cities in locations['Asia'].items():
    for city in cities:
        asia_cities.append('{} - {}'.format(city, country))
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print (city)