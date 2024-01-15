class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# ---------------------------------------------------------------------------------------------------------------------------
"""
Task 1. Write definition of prepend() function and test its functionality
"""
# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    new_head = Node(value)
    
    if self.head is None:
        self.head = new_head
    else:
        new_head.next = self.head
        self.head = new_head
    pass


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"


# ---------------------------------------------------------------------------------------------------------------------------
"""
Task 2. Write definition of append() function and test its functionality
"""
def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here  
    if self.head is None:
        self.head = Node(value)
        return
    # Move to the tail (the last node)
    node = self.head
    while node.next:
        node = node.next
    node.next = Node(value)

    return

LinkedList.append = append

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"


# ---------------------------------------------------------------------------------------------------------------------------
"""
Task 3. Write definition of search() function and test its functionality
"""
def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    current_node = self.head
    while current_node:
        if current_node.value == value:
            return current_node
        current_node = current_node.next
    return None

LinkedList.search = search

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"


# ---------------------------------------------------------------------------------------------------------------------------
"""
Task 4. Write definition of remove() function and test its functionality
"""
def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    current_node = self.head
    
    if current_node and current_node.value == value:
        self.head = current_node.next
        return
    
    prev_node = None
    # The while loop breaks once the first instance of the selected node is reached
    while current_node and current_node.value != value:
        prev_node = current_node
        current_node = current_node.next

    # If the target is not present in the linked list
    if not current_node:
        return

    # Update the pointers to remove the target node
    prev_node.next = current_node.next
    return

LinkedList.remove = remove

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"


# ---------------------------------------------------------------------------------------------------------------------------
"""
Task 5. Write definition of pop() function and test its functionality
"""
def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    node = self.head
    self.head = node.next
    return node.value

LinkedList.pop = pop

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"