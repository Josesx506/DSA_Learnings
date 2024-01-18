"""
Create a sorted linked list
    Given a stream of random integers, create a linked list that is always sorted from ascending 
    order (lowest to highest). What's the computational complexity of adding an element in this way?
"""
# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)

class SortedLinkedList:
    def __init__(self):
        self.head = None
        
    def get_min(self):
        """Get the minimum value of a linked list"""
        min_val = None
        
        current_node = self.head
        while current_node:
            if min_val is None or current_node.value<min_val:
                min_val = current_node.value
            current_node = current_node.next
        
        return min_val
        
    def get_max(self):
        """Get the maximum value of a linked list"""
        max_val = None
        
        current_node = self.head
        while current_node is not None:
            if max_val is None or current_node.value>max_val:
                max_val = current_node.value
            current_node = current_node.next
        
        return max_val
    
    # My implementation that isn't efficient but it always returns a sorted list
    # It relies on the min and max functions above
    # def append(self, value):
    #     """
    #     Append a value to the Linked List in ascending sorted order
    #     Args:
    #        value(int): Value to add to Linked List
    #     """
    #     # TODO: Write your sorted append function here
    #     if self.head is None:
    #         self.head = Node(value)
        
    #     elif self.head.value > value and value < self.get_min():
    #         new_node = Node(value)
    #         new_node.next = self.head
    #         self.head = new_node
        
    #     else:
    #         llist = self.head
            
    #         while llist.next is not None:
    #             if llist.value < value and value < llist.next.value and value < self.get_max():
    #                 new_node = Node(value)
    #                 new_node.next = llist.next
    #                 llist.next = new_node
    #                 return
    #             else:
    #                 llist = llist.next
            
    #         if llist.value < value:
    #             llist.next = Node(value)     
    #     return
    
    # Udacity implementation that is more efficient
    # Computational complexity is  𝑂(𝑁) where  𝑁 is the current length of the linked list.
    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order
        Args:
           value(int): Value to add to Linked List
        """
        if self.head is None:
            self.head = Node(value)
            return
        
        if value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return
        
        node = self.head
        while node.next is not None and value >= node.next.value:
            node = node.next
            
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        
        return None
    
    # I included the iterate and print functions so the values of the linked list can be viewed
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
    
    def __repr__(self):
        return str([v for v in self])

# Test cases
linked_list = SortedLinkedList()
linked_list.append(3)
print ("Pass" if (linked_list.head.value == 3) else "Fail")

linked_list.append(2)
print ("Pass" if (linked_list.head.value == 2) else "Fail")

linked_list.append(4)
node = linked_list.head.next.next
print ("Pass" if (node.value == 4) else "Fail")

# Append additional items to be tested
linked_list.append(9)
linked_list.append(1)
linked_list.append(7)
linked_list.append(5)
linked_list.append(6)
print(linked_list)


"""
Additional question: Sort an array with this linked list
    Given an array of integers, use this linked list to sort them and return a sorted array. 
    What's the computational complexity of this sorting algorithm? How does it compare to other 
    sorting algorithms?
"""
# My sorting implementation that works because of the iteration function above
def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.
    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    sorted_ll = SortedLinkedList()
    # TODO: Write your sorting function here
    for i in array:
        sorted_ll.append(i)
    
    out_list = [v for v in sorted_ll]
    
    return out_list

# Test case
print ("Pass" if (sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")

# Udacity solution that works without the iteration function above
def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.
    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    sorted_array = []
    
    linked_list = SortedLinkedList()
    for value in array:
        linked_list.append(value)
    
    # Convert sorted linked list to a normal list/array
    node = linked_list.head
    while node:
        sorted_array.append(node.value)
        node = node.next
    
    return sorted_array

"""
Check out the readme for this chapter to see the overall computational complexity
"""