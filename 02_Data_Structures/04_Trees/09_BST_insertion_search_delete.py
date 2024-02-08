'''
Perform insertion and search comparisons within this notebook i.e. check whether the search value is equal to a node or not
'''
# ------------------------------------------------ Node Class ------------------------------------------------
# this code makes the tree that we'll traverse
class Node(object):
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"


# ------------------------------------------------ Queue Class ------------------------------------------------
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


'''
Define INSERT

Let's assume that duplicates are overriden by the new node that is to be inserted. Other options are to keep a counter 
of duplicate nodes, or to keep a list of duplicates nodes with the same value.

    - Use a while loop
    - Use a recursive function
'''
class Tree():
    def __init__(self):
        self.root = None
        
    def set_root(self,value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
    
    """
    @TODO: define insert here
    can use a for loop (try one or both ways)
    """
            
    def insert_with_loop(self,new_value):
        # ADD YOUR CODE HERE
        node = self.get_root()
        
        if node is None:
            self.set_root(new_value)
            return
        
        new_node = Node(new_value)

        while(True):
            comparison = self.compare(node, new_node)
            
            if comparison == 0:
                print("Equal nodes are being replaced")
                node.set_value(new_node.get_value())
                return
            elif comparison == -1:
                # Shift to the left node if it exists
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    print(f"{new_node} is being inserted to left of {node}")
                    node.set_left_child(new_node)
                    return
            else:
                # Shift to the right node if it exists
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    print(f"{new_node} is being inserted to right of {node}")
                    node.set_right_child(new_node)
                    return


    """
    @TODO: define insert here (can use recursion)
    try one or both ways
    """  
    def insert_with_recursion(self,value):
        # ADD YOUR CODE HERE
        node = self.get_root()
        
        if node is None:
            self.set_root(value)
            return
        
        newNode = Node(value)
        self.insert_recursively(node, newNode)
    
    def insert_recursively(self, node, new_node):
        comparison = self.compare(node, new_node)
        if comparison == 0:
            # Replace the current node value only if they're equal
            node.set_value(new_node.get_value())
            return
        elif comparison == -1:
            # Shift to the left node if it exists
            if node.has_left_child():
                # Recursively update the left node if it exists
                self.insert_recursively(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)
                return
        else:
            # Shift to the right node if it exists
            if node.has_right_child():
                # Recursively update the right node if it exists
                self.insert_recursively(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)
                return
    
                    
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


# Test implementation for while loop INSERT
tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(5) # insert duplicate
tree.insert_with_loop(1)
tree.insert_with_loop(8)
tree.insert_with_loop(7)
tree.insert_with_loop(9)
tree.insert_with_loop(3)
print(tree)

# Test implementation for recursion INSERT
tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5) # insert duplicate
tree.insert_with_recursion(1)
tree.insert_with_recursion(8)
tree.insert_with_recursion(7)
tree.insert_with_recursion(9)
tree.insert_with_recursion(3)
print(tree)

'''
Define SEARCH

Define a search function that takes a value, and returns true if a node containing that value exists in the tree, otherwise false.
'''
class Tree():
    def __init__(self):
        self.root = None
        
    def set_root(self,value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node 
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
    
    def insert(self,new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node
                node = new_node
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping
                    
    """
    @TODO: implement search
    """
    def search(self,value):
        # ADD YOUR CODE HERE
        node = self.get_root()
        
        while node is not None:
            if value > node.get_value() and node.has_right_child():
                node = node.get_right_child()
            elif value < node.get_value() and node.has_left_child():
                node = node.get_left_child()
            elif value == node.get_value():
                return True
            else:
                return False
    

    # Udacity Solution for search
    # def search(self,value):
    #     node = self.get_root()
    #     s_node = Node(value)
    #     while(True):
    #         comparison = self.compare(node,s_node)
    #         if comparison == 0:
    #             return True
    #         elif comparison == -1:
    #             if node.has_left_child():
    #                 node = node.get_left_child()
    #             else:
    #                 return False
    #         else:
    #             if node.has_right_child():
    #                 node = node.get_right_child()
    #             else:
    #                 return False

                    
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


# Test the search function
tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)
tree.insert(1)

print(f"""
search for 8: {tree.search(8)}
search for 2: {tree.search(2)}
search for 1: {tree.search(1)}
search for 9: {tree.search(9)}
""")
print(tree)


'''
Bonus: DELETE

Try implementing deletion yourself. You can also check out this explanation here

There are three types of delete cases
    - Case 1: Leaf node
    - Case 2: node had one child node
    - Case 3: node has two child nodes

Solution is from Geek for Geeks
'''
# Python3 program to implement optimized delete in BST.

class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=' ')
		inorder(root.right)

# A utility function to insert a new node with given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node

# Given a binary search tree and a key, this function
# deletes the key and returns the new root
def deleteNode(root, k):
	# Base case
	if root is None:
		return root

	# Recursive calls for ancestors of
	# node to be deleted
	if root.key > k:
		root.left = deleteNode(root.left, k)
		return root
	elif root.key < k:
		root.right = deleteNode(root.right, k)
		return root

	# We reach here when root is the node
	# to be deleted.

	# If one of the children is empty
	if root.left is None:
		temp = root.right
		del root
		return temp
	elif root.right is None:
		temp = root.left
		del root
		return temp

	# If both children exist
	else:

		succParent = root

		# Find successor
		succ = root.right
		while succ.left is not None:
			succParent = succ
			succ = succ.left

		# Delete successor. Since successor
		# is always left child of its parent
		# we can safely make successor's right
		# right child as left of its parent.
		# If there is no succ, then assign
		# succ.right to succParent.right
		if succParent != root:
			succParent.left = succ.right
		else:
			succParent.right = succ.right

		# Copy Successor Data to root
		root.key = succ.key

		# Delete Successor and return root
		del succ
		return root

# Driver Code
# if __name__ == '__main__':
# Let us create following BST
#	  50
#   /    \
#  30    70
#  / \   / \
# 20 40 60 80
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)

print("Original BST: ", end='')
inorder(root)

print("\n\nDelete a Leaf Node: 20")
root = deleteNode(root, 20)
print("Modified BST tree after deleting Leaf Node:")
inorder(root)

print("\n\nDelete Node with single child: 70")
root = deleteNode(root, 70)
print("Modified BST tree after deleting single child Node:")
inorder(root)

print("\n\nDelete Node with both child: 50")
root = deleteNode(root, 50)
print("Modified BST tree after deleting both child Node:")
inorder(root)

