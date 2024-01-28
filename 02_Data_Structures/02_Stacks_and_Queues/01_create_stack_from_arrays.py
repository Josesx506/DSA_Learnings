class Stack:
    
    def __init__(self, initial_size = 10):
        '''You can use zero or None to initialize but I prefer None'''
        self.arr = [None for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
    
    def push(self, data):
        '''
        Increment the index and num elements everytime a push is done
        If the number of items being pushed exceed the length of the array,
            extend the length of the array
        '''

        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        '''
        This handles dynamically lengthening the array when the
            capacity is reached
        It first creates a copy of the original array, creates a new array
            that's twice the length of the old array, repopulates the 
            new array with the old array values
        Note: Copying items many times can be slow
        '''
        old_arr = self.arr

        self.arr = [0 for _ in range( 2* len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element
    
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
        Decrement the index and num elements everytime a pop is done
        If the stack is empty, return None else return the last inserted item.
        '''
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]


# Tests
foo = Stack()
print(foo.size()) # Should return 0
print(foo.is_empty()) # Should return True
foo.push("Test") # Let's push an item onto the stack and check again
print(foo.size()) # Should return 1
print(foo.is_empty()) # Should return False
foo.push("Test") # We first have to push an item so that we'll have something to pop
print(foo.pop()) # Should return the popped item, which is "Test"
print(foo.pop()) # Should return None, since there's nothing left in the stack
foo.push(1)
foo.push(2)
foo.push(3)
foo.push(4)
foo.push(5)
foo.push(6)
foo.push(7)
foo.push(8)
foo.push(9)
foo.push(10) # The array is now at capacity!
foo.push(11) # This one should cause the array to increase in size
print(foo.arr) # Let's see what the array looks like now!
# If we successfully doubled the array size, it should now be 20.
print("Pass" if len(foo.arr) == 20 else "Fail")