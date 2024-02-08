'''
Think through the algorithm
We are walking down the tree one level at a time. So we start with apple at the root, and next are banana and cherry,
and next is dates.

1) start at the root node
2) visit the root node's left child (banana), then right child (cherry)
3) visit the left and right children of (banana) and (cherry).

Queue
Notice that we're waiting until we visit "cherry" before visiting "dates". It's like they're waiting in line. We can use 
a queue to keep track of the order.
'''


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


# -------------------------------------------- create a tree and add some nodes --------------------------------------------
tree = Tree("apple")  # root node
tree.get_root().set_left_child(Node("banana"))  # set first level's left child
tree.get_root().set_right_child(Node("cherry"))  # set first level's right child
tree.get_root().get_left_child().set_left_child(Node("dates")) # set second level's left child by getting the first level's left child first


# Define a Queue class
# import deque datatype from collections module
from collections import deque
# instantiate a deque object
q = deque()
# add 2 elements to the left of the deque
q.appendleft("apple")
q.appendleft("banana")
print(q)
# remove and return the most right element of the list
q.pop()
print(q)
len(q)


from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

q = Queue()
q.enq("apple")
q.enq("banana")
q.enq("cherry")
print(q)
print(q.deq()) # Dequeue
print(q)

# Queue items being traversed on the tree
visit_order = list()
q = Queue()

# start at the root node [Level 01] and add it to the queue
node = tree.get_root()
q.enq(node)
print(q)

# Enter [Level 02] dequeue the root node in the queue. 
# When the queue returns the node, "visit" that node and add its children to the queue
node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())
    
print(f"visit order: {visit_order}")
print(q)


# Level 02, dequeue the left child node (banana)
# visit it, and add its children (dates) to the queue 
node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())
    
print(f"visit order: {visit_order}")
print(q)


# Level 02, dequeue the right child node (cherry)
# visit it, and add its children (there are None) to the queue 
node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())
    
print(f"visit order: {visit_order}")
print(q)

# Level 03 - dequeue the left node (dates) of banana
# visit it, and add its children (there are None) to the queue 
node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())
    
print(f"visit order: {visit_order}")
print(q)



# ------------------------------------------------ BFS algorithm with while loop ------------------------------------------------
def bfs(tree):
    # queue
    q = Queue()
    # visit_order
    visit_order = list()
    # Start at the root node
    node = tree.get_root()
    # Add the root to queue
    q.enq(node)
    
    while(node):
        # Dequeue the node
        node = q.deq()
        # visit the node
        visit_order.append(node)

        # Add the left child if it exists
        if node.has_left_child():
            q.enq(node.get_left_child())
        
        # Add the right child if it exists
        if node.has_right_child():
            q.enq(node.get_right_child())
        
        # You can also use len(q)>0 at the top of the while loop and remove the else statement
        else:
            if len(q) == 0:
                node = None
    
    return visit_order

# check solution: should be: apple, banana, cherry, dates
bfs(tree)


'''
Bonus Task: write a print function
Define the print function for the Tree class. Nodes on the same level are printed on the same line.

For example, the tree we've been using would print out like this:

Node(apple)
Node(banana) | Node(cherry)
Node(dates) | <empty> | <empty> | <empty>
<empty> | <empty>
We'll have <empty> be placeholders so that we can keep track of which node is a child or parent of the other nodes.

hint: use a variable to keep track of which level each node is on. For instance, the root node is on level 0, and 
its child nodes are on level 1.
'''
# solution

class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )
                
            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )
                
        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

        return s

# check solution
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
print(tree)
