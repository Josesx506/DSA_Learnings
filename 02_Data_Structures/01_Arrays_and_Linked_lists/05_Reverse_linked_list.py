"""
Given a singly linked list, return another linked list that is the reverse of the first.
"""

# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])


"""
Write the function definition here
"""
def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    
    # TODO: Write your function to reverse linked lists here
    new_list = LinkedList()
    
    prev_node = None                        # Make this none since this will be the tail of the reversed list
    
    # In this "for" loop, the "value" is just a variable whose value will be updated in each iteration
    for value in linked_list:
        # create a new node
        new_node = Node(value)
        new_node.next = prev_node           # Change the link of the next node to be the previous node
        prev_node = new_node                # Mark the current new node as the "prev_node" for next iteration
    
    # Update the new_list.head to point to the final node that came out of the loop
    new_list.head = prev_node
    
    # The syntax below reverses the linked-list but throws an error on the second tes
    # prev_node = None                        # Make this none since this will be the tail of the reversed list
    # current_node = linked_list.head         # Extract the head of the linked list
    
    # while current_node is not None:
    #     next_node = current_node.next       # Extract the next node
    #     current_node.next = prev_node       # Change the link of the next node to be the previous node
    #     prev_node = current_node            # Update the previous node to the current node
    #     current_node = next_node            # Update the current node to check the next node
    
    # new_list.head = prev_node               # Reversed linked list is in the prev_node variable
    
    return new_list

# Tests
llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")