'''Traverse a tree (depth first search)

Traversing a tree means "visiting" all the nodes in the tree once. Unlike an array or linked list, there's more 
than one way to walk through a tree, starting from the root node.

Traversing a tree is helpful for printing out all the values stored in the tree, as well as searching for a value 
in a tree, inserting into or deleting values from the tree. There's depth first search and breadth first search.

Depth first search has 3 types: pre-order, in-order, and post-order.
'''
# Starter code that makes the tree that we'll traverse
class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
    
    # set value of the node
    def set_value(self,value):
        self.value = value
    
    # get value of the node
    def get_value(self):
        return self.value
    
    # set a node for the left child
    def set_left_child(self,left):
        self.left = left
    
    # set a node for the right child
    def set_right_child(self, right):
        self.right = right
    
    # get the node of left child
    def get_left_child(self):
        return self.left
    
    # get the node of right child
    def get_right_child(self):
        return self.right

    # check if node has left child -> return boolean
    def has_left_child(self):
        return self.left != None
    
    # check if node has right child -> return boolean
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

# create a tree and add some nodes
tree = Tree("apple")  # root node

# set first level's left child
tree.get_root().set_left_child(Node("banana"))  

# set first level's right child
tree.get_root().set_right_child(Node("cherry"))  

# set second level's left child 
# by getting the first level's left child first
tree.get_root().get_left_child().set_left_child(Node("dates"))


'''
Stack

Notice how we're retracing our steps. It's like we are hiking on a trail, and trying to retrace our steps on the way back. 
This is an indication that we should use a stack.
'''
# Let's define a stack to help keep track of the tree nodes
class Stack():
    def __init__(self):
        self.list = list()
    
    # add an element to the list
    def push(self,value):
        self.list.append(value)
        
    # remove the last element from the list
    def pop(self):
        return self.list.pop()
        
    # get the value of the last element in the list
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
    
    # check if the list empty
    def is_empty(self):
        return len(self.list) == 0
    
    # 
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"


# instantiate Stack
stack = Stack()
# add elements into the stack
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
# remove and print the last element (top of the stack)
print(stack.pop())
print("\n")
print(stack)


# ------------------------------------------ Begin Pre-order Traversal ------------------------------------------
visit_order = list()
stack = Stack()

# Level 01 - start at the root node, visit it and then add it to the stack ............................
node = tree.get_root()
stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# Update the visit_order list to indicate we've visited the root node - apple
visit_order.append(node.get_value())
print(f"""visit order {visit_order}
{stack}
""")

# Level 02 - check if apple (root) has a left child...........................................
print(f"{node} has left child? {node.has_left_child()}")
# since apple has a left child (banana) we'll visit banana and add it to the stack
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# visit banana (first level's left child)
print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order {visit_order}""")


# Level 03 - check if banana has a left child (second level's left chile)........................
print(f"{node} has left child? {node.has_left_child()}")

# since banana has a left child "dates" we'll visit "dates" and add it to the stack
if node.has_left_child():
    node = node.get_left_child()    
    stack.push(node)
    
print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# visit dates (second level's left chile)
visit_order.append(node.get_value())
print(f"visit order {visit_order}")

# Leaf node checklist.............................................................................
# check if "dates" has a left child -> return boolean value
print(f"{node} has left child? {node.has_left_child()}")
# since dates doesn't have a left child, we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")
# since "dates" is a leaf node (has no children), we can start to retrace our steps
# in other words, we can pop it off the stack.
print(stack.pop())
print(stack)




# Return to level 02 - now we'll set the node to the new top of the stack, which is banana
node = stack.top()
print(node)
# we already checked for banana's left child, so we'll check for its right child
print(f"{node} has right child? {node.has_right_child()}")
# banana doesn't have a right child, so we're also done tracking it. so we can pop banana off the stack
print(f"pop {stack.pop()} off stack")
print(f"""
stack
{stack}
""")


# Return to level 01 - now we'll track the new top of the stack, which is apple
node = stack.top()
print(node)
# we've already checked if apple has a left child; we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")


# Since it has a right child (cherry) proceed tp Level 02, we'll visit cherry and add it to the stack.
if node.has_right_child():
    node = node.get_right_child()
    stack.push(node)
    
print(f"""
visit_order {visit_order} 
stack
{stack}
""")
# visit cherry (first level's right child)
print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order: {visit_order}""")

# Now we'll check if cherry (first level's right child) has a left child
print(f"{node} has left child? {node.has_left_child()}")
# it doesn't, so we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")

# since cherry has neither left nor right child nodes,
# we are done tracking it, and can pop it off the stack
print(f"pop {stack.pop()} off the stack")

print(f"""
visit_order {visit_order} 
stack
{stack}
""")

# now we're back to apple at the top of the stack. since we've already checked apple's left and right 
# child nodes, we can pop apple off the stack
print(f"pop {stack.pop()} off stack")
print(f"pre-order traversal visited nodes in this order: {visit_order}")

print(f"""stack
{stack}""")