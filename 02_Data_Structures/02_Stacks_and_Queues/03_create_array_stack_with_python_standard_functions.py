'''
 Python 3.x conviently allows us to demonstate this functionality with a list. 
 When you have a list such as [2,4,5,6] you can decide which end of the list is 
 the bottom and the top of the stack respectivley. Once you decide that, you 
 can use the append, pop or insert function to simulate a stack. We will choose 
 the first element to be the bottom of our stack and therefore be using the append 
 and pop functions to simulate it. Give it a try by implementing the function below!
'''

class Stack():
    def __init__(self):
        # TODO: Initialize the Stack
        self.items = []
        self.next_index = 0
        self.num_elements = 0
    
    def size(self):
        # TODO: Check the size of the Stack
        return self.num_elements
    
    def push(self, item):
        # TODO: Push item onto Stack
        self.items.append(item)
        self.next_index += 1
        self.num_elements += 1

    def pop(self):
        # TODO: Pop item off of the Stack
        if self.num_elements == 0:
            return None
        else:
            self.next_index -= 1
            self.num_elements -= 1
            item = self.items[self.next_index]
            self.items.pop()
            return item

# Test the stack
MyStack = Stack()
MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")