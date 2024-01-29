class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    # TODO: Add the enqueue method
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node   # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next  # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
            
    # Add the dequeue method
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            self.num_elements -= 1
            return value
    
    # TODO: Add the size method
    def size(self):
        return self.num_elements
    
    # TODO: Add the is_empty method
    def is_empty(self):
        return self.num_elements == 0

# Test Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")