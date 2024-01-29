class Queue:
    def __init__(self):
        # TODO: Initialize the Queue
        self.items = []
    
    def size(self):
        # TODO: Check the size of the Queue
        return len(self.items)
    
    def enqueue(self, item):
        # TODO: Enter item into Queue
        self.items.append(item)

    def dequeue(self):
        # TODO: Remove item from the Queue
        if self.size() == 0:
            return None
        else:
            return self.items.pop(0)

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


# Udacity Solution - Performing dequeue on an empty Queue will throw an error
class Queue:
    def __init__(self):
         self.storage = []
    
    def size(self):
         return len(self.storage)
    
    def enqueue(self, item):
         self.storage.append(item)

    def dequeue(self):
         return self.storage.pop(0)

        
# Setup
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
