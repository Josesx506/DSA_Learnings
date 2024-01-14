"""
Exercise 1. Reverse Strings
For example, if the input is the string "water", then the output should be "retaw"
"""
# Code

def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    reverse = ""
    length = len(our_string)
    # TODO: Write your solution here
    for i in range(length,0,-1):
        reverse += our_string[i-1]
    
    return reverse

# Test Cases
print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")


"""
Exercise 2. Anagrams
The goal of this exercise is to write some code to determine if two strings are anagrams of each other.
An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).

For example:
- "rat" is an anagram of "art"
- "alert" is an anagram of "alter"
- "Slot machines" is an anagram of "Cash lost in me"

Note - You can use built-in methods len(), lower() and sort() on strings.
"""
# Code

def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    # TODO: Write your solution here
    # convert all the strings to lower case
    str1,str2 = sorted(str1.replace(" ","").lower()),sorted(str2.replace(" ","").lower())
    
    if str1 == str2:
        return True
    else:
        return False

# Test Cases
print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")


"""
Exercise 3. Reverse the words in sentence
Given a sentence, reverse each word in the sentence while keeping the order the same!
"""
def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    # TODO: Write your solution here
    str_list = our_string.split(" ")
    
    flipped = ""
    
    for word in str_list:
        flipped += word[::-1]+" "
    
    return flipped.strip()

# Test Cases
print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")


"""
Exercise 4. Hamming Distance
In information theory, the Hamming distance between two strings of equal length is the number of positions at which 
the corresponding symbols are different. Calculate the Hamming distace for the following test cases.
"""
# Code

def hamming_distance(str1, str2):
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    
    # TODO: Write your solution here
    if len(str1) == len(str2):
        dist = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                dist += 1
        return dist
    else:
        return None

# Test Cases
print ("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print ("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
print ("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print ("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
print ("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")