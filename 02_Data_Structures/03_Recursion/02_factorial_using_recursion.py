'''
Factorial using recursion
The factorial function is a mathematical function that multiplies a given number, n, and all of the
whole numbers from n down to 1.

For example, if n is  4 then we will get:

4 * 3 * 2 * 1 = 24
 
This is often notated using an exclamation point, as in  4!
  (which would be read as "four factorial").

So  4! = 4 * 3 * 2 * 1 = 24
'''

# Code
def factorial(n):
    """
    Calculate n!
    
    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    
    # TODO: Write your recursive factorial function here
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test Cases
print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")