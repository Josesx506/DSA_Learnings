class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)         # Create the first node in the linked-list aka head node
head.next = Node(1)    # Append a new node to the end of the list

# Add three more nodes to the list, with the values 4, 3, and 5
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

# Let's print the values of all the nodes to check if it worked.
print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)


"""
Exercise 2 - Traversing the list

We successfully created a simple linked list. But printing all the values like we did above was pretty tedious. 
What if we had a list with 1,000 nodes?
Let's see how we might traverse the list and print all the values, no matter how long it might be.
"""

def print_linked_list(head):
    # Start with the current node as the head
    current_node = head
    
    # While you're not at the end of the list
    while current_node is not None:
        print(current_node.value)
        # Change the current node to the next node in the linked-list
        current_node = current_node.next

print_linked_list(head)


"""
Exercise 3 - Creating a linked list using iteration

The function should take a Python list of values as input and return the head of a linked list that has those values
There's some test code, and also a solution, below—give it a try for yourself first, but don't hesitate to look over the solution if you get stuck
"""
def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list

    This has a Big-O complexity of n**2 because the list is being traversed twice
    for and while loops to find the last item and update it
    """
    head = None
    
    for value in input_list:
        if head is None:
            head = Node(value)    
        else:
            # Move to the tail (the last node)
            current_node = head
            while current_node.next:
                current_node = current_node.next
        
            current_node.next = Node(value)
        
    return head

# Tests
### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)

input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list(input_list)
test_function(input_list, head)


"""
A more efficient solution
The above solution works, but it has some shortcomings. In this next walkthrough, we'll demonstrate a different approach and see how its efficiency compares to the solution above.
"""
def create_linked_list_better(input_list):
    """This has a Big-O complexity of n because of the single `for` loop"""
    # Create head and tail variables
    head = None
    tail = None
    
    for value in input_list:
        # If the head does not exist
        if head is None:
            # Create a new head
            head = Node(value)
            # Assign the new head as the last node in the linked-list
            tail = head            
        else:
            # Link the tail node to the new node
            tail.next = Node(value)
            # Make sure the new node is assign as the tail of the linked-list
            tail = tail.next        # update the tail
            
    return head

### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)

input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list_better(input_list)
test_function(input_list, head)
