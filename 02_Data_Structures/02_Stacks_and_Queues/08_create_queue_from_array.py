
class Queue:
    def __init__(self, initial_size = 10):
        '''
        front_index is set to -1 because 0 will indicate it has been initialized
        '''
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0
    
    def enqueue(self, value):
        '''
        Enqueue new element. 
        Use modulo for the next element to ensure it doesn't exceed the length of the array
        '''
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0
    
    # TODO: Add the size method
    def size(self):
        return self.queue_size

    # TODO: Add the is_empty method
    def is_empty(self):
        return self.queue_size == 0

    # TODO: Add the front method
    def front(self):
        if self.is_empty():
            return None
        else:
            return self.arr[self.front_index]

    # TODO: Add the dequeue method
    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1   # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element - Modulo is used to avoid skipping old head elements that have been dequeued
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value
    
    # TODO: Add the _handle_queue_capacity_full method
    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]

        index = 0

        # copy all elements from front of queue (front-index) until end
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # case: when front-index is ahead of next index i.e the next index has rolled over to the 
        #   beginning of the array because of the modulo
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # reset pointers
        self.front_index = 0
        self.next_index = index


# Unit tests Setup
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