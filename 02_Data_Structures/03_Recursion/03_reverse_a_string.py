# Code
def reverse_string(input_str):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """
    # TODO: Write your recursive string reverser solution here
    if len(input_str) == 0:
        # If the string is empty, break the loop
        return ""
    else:
        first_char = input_str[0]       # Get the first value of the string
        remaining_char = input_str[1:]  # Get all other items after the first item
        
        # Move the first item to the back of the string and recursively iterate to the next item
        return reverse_string(remaining_char) + first_char


# Test Cases  
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")

# Udacity Solution
"""
RECURSIVE FUNCTION
Args: input(str): string to be reversed
Returns: a string that us reversed of input
"""
def reverse_string(input):
    
    # (Recursion) Termination condition / Base condition
    if len(input) == 0:
        return ""

    else:
        first_char = input[0]
        
        '''
        The `slice()` function can accept upto the following three arguments.
        - start: [OPTIONAL] starting index. Default value is 0.
        - stop: ending index (exclusive)
        - step_size: [OPTIONAL] the increment size. Default value is 1.
        
        The return type of `slice()` function is an object of class 'slice'. 
        '''
        the_rest = slice(1, None)     # `the_rest` is an object of type 'slice' class
        sub_string = input[the_rest]  # convert the `slice` object into a list
        
        # Recursive call
        reversed_substring = reverse_string(sub_string)
        
        return reversed_substring + first_char
#-------------------------------------------------#
'''
**Time and Space Complexity Analysis**
Each recursive call to the `reverse_string()` function will create 
a new set of local variables - first_char, the_rest, sub_string, and reversed_substring. 
Therefore, the space complexity of a recursive function would always be proportional to the 
maximum depth of recursion stack.  
The time complexity for this function will be  O(k*n), where k is a constant and n is the 
number of characters in the string (depth of recursion stack). 
'''

'''
This can also be solved by adding a length argument to access the string properties from the tail end
'''
def reverse(string, length):
    if length < 1:
        return ""
     
    # Base case
    if length == 1:
        return string[0]
 
    return string[length - 1] + reverse(string, length - 1)
