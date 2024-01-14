
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

"""
Usually you'll want to create a LinkedList class as a wrapper for the nodes 
themselves and to provide common methods that operate on the list.

Note that if we're only tracking the head of the list, this runs in 
linear time -  O(n) - since you have to iterate through the entire list to get to the tail node. 
However, prepending (adding to the head of the list) can be done in constant  O(1) time
"""
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

        return
    
    def to_list(self):
        # TODO: Write function to turn Linked List into Python List
        list_container = []
        node = self.head
        
        while node:
            list_container.append(node.value)
            node = node.next
        
        return list_container
    
# Test your method here
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")


"""
2. Doubly Linked Lists
This type of list has connections backwards and forwards through the list.

Now that we have backwards connections it makes sense to track the tail of the linked list as well as the head.

Exercise: Implement a doubly linked list that can append to the tail in constant time. Make sure to include 
forward and backward connections when adding a new node to the list.
"""
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        # TODO: Implement this method to append to the tail of the list
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        # Move to the tail (the last node)
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
    
# Test your class here
linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous