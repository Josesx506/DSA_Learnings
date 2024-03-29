'''
Assume you are planning to take additional courses at your local educational institution, and you 
have acquired some data about the available courses and when they will be offered. In the following 
exercise, you will write control structures to process the data and return the semesters when a 
given course is offered.

You will need to complete the function when_offered(courses, course). This function accepts a "courses" 
data structure and a "course" string. The function should return a list of strings representing the 
semesters when the input course is offered. See the two test cases below for examples of correct results.
'''


# This exercise uses a data structure that stores course information.
# The data structure format is:
#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }
courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }
def when_offered(courses, course):
    # TODO: Fill out the function here.
    semester_list = []

    for k,v in courses.items():
        semester_courses = list(v.keys())
        if course in semester_courses:
            semester_list.append(k)
    
    # TODO: Return list of semesters here.
    return semester_list


print(when_offered(courses, 'cs101'))
# Correct result: 
# ['fall2020', 'spring2020']
print(when_offered(courses, 'bio893'))
# Correct result: 
# []