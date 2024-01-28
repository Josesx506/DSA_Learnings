# Add the Node class here
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    # TODO: Add the __init__ method
    def __init__(self):
        self.head = None
        self.num_elements = 0
    
    def push(self, value):
        '''
        You can push to the head or tail of a linklist however, pushing
            to the tail will always have a complexity of O(n) whereas
            pushing to the head has a complexity of O(1)
        Note: After pushing, increment the number of elements by 1
        '''
        new_node = Node(value)  

        # if stack is empty
        if self.head is None:
            self.head = new_node
        
        else:
             # place the new node at the head of the linked list (top)
            new_node.next = self.head
            self.head = new_node
        
        # or should we add it to the tail?
        # else:
        #     current_node = head
        #     while current_node.next:
        #         current_node = current_node.next
        #     current_node.next = new_node

        self.num_elements += 1
        
    # TODO: Add the size method
    def size(self):
        return self.num_elements
    
    # TODO: Add the is_empty method
    def is_empty(self):
        '''
        Checks whether the number of elements is zero or not
        returns Boolean
        '''
        return self.num_elements == 0

    def pop(self):
        '''
        This pop implementation assumes push was done at the head of the stack
        Note: After popping, decrement the number of elements by 1
        '''
        # if stack is empty
        if self.head is None:
            return None
        else:
            current_node = self.head
            self.head = self.head.next
            self.num_elements -= 1
            return current_node.value

# Tests Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")