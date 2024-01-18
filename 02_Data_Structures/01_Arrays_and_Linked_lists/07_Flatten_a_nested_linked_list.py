"""
Flattening a nested linked list
    Suppose you have a linked list where the value of each node is a sorted linked list (i.e., 
        it is a nested list). Your task is to flatten this nested list—that is, to combine all 
        nested lists into a single (sorted) linked list.
"""
# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones. 
# User defined class
class Node:
    def __init__(self, value): # <-- 
        '''
        For simple LinkedList, "value" argument will be an int, whereas, 
        for NestedLinkedList, "value" will be a LinkedList
        '''
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
# User defined class
class LinkedList: 
    def __init__(self, head): # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head
    
    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''
    def append(self, value):
        
        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return
        
        # Create a temporary Node object
        node = self.head
        
        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next
        
        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

        
    '''We will need this function to convert a LinkedList object into a Python list of integers'''
    def to_list(self):
        out = []                # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object
        
        while node:       # <-- Iterate untill we have nodes available
            #  node.value is actually of type Node, therefore convert it into int before appending to the Python list
            out.append(int(str(node.value))) # <--
            node = node.next
        
        return out


"""
Exercise - Write the two function definitions below
    Now, in the cell below, see if you can solve the problem by implementing the flatten method.
    Hint: If you first create a merge method that merges two linked lists into a sorted linked list, 
        then there is an elegant recursive solution.
"""
def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    merged = LinkedList(None) # Create an empty linked list
    
    # If either of the input lists are none, return the non-empty list
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    
    # Sort an append to the new linked list
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)   # append to the merge link-list
            list2_elt = list2_elt.next # Increment to the next node
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value: # Check which value is larger to sort
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(LinkedList):  
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        return self._flatten(self.head) # <-- self.head is a node for NestedLinkedList

    '''  A recursive function ''' 
    def _flatten(self, node):
        
        # A termination condition
        if node.next is None:
            return merge(node.value, None) # <-- First argument is a simple LinkedList
        
        # _flatten() is calling itself untill a termination condition is achieved
        return merge(node.value, self._flatten(node.next)) # <-- Both arguments are a simple LinkedList each

# Test cases
# First Test scenario
''' Create a simple LinkedList'''
linked_list = LinkedList(Node(1)) # <-- Notice that we are passing a Node made up of an integer
linked_list.append(3) # <-- Notice that we are passing a numerical value as an argument in the append() function here 
linked_list.append(5)

''' Create another simple LinkedList'''
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

''' Create a NESTED LinkedList, where each node will be a simple LinkedList in itself'''
nested_linked_list = NestedLinkedList(Node(linked_list)) # <-- Notice that we are passing a Node made up of a simple LinkedList object
nested_linked_list.append(second_linked_list) # <-- Notice that we are passing a LinkedList object in the append() function here

"""
Structure of the nested linked list to be tested
    nested_linked_list should now have 2 nodes. The head node is a linked list containing 1, 3, 5. 
        The second node is a linked list containing 2, 4.
    Calling flatten should return a linked list containing 1, 2, 3, 4, 5.
"""
solution = nested_linked_list.flatten() # <-- returns A LinkedList object

expected_list = [1,2,3,4,5] # <-- Python list

# Convert the "solution" into a Python list and compare with another Python list
assert solution.to_list() == expected_list, f"list contents: {solution.to_list()}"

"""
Check the readme for the computational complexity
"""