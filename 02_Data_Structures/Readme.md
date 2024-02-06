### Table of contents
- [Arrays and Linked Lists](#arrays-and-linked-lists)
- [Stacks and Queues](#stacks-and-queues)
- [Recursion](#recursion)
- [Trees](#trees)


## Arrays and Linked Lists
**Arrays** <br>
When an array is created, it is always given some initial size—that is, the number of elements it should be able to hold (and how large each element is).The computer then finds a block of memory and sets aside the space for the array. Importantly, the space that gets set aside is one, continuous block. That is, all of the elements of the array are *contiguous*, meaning that they are all next to one another in memory. Because of the adjacent locations of array items in memory, we can assign each item an index and use that index to quickly and directly access the item. <br>
Another key characteristic of an array is that **all of the elements** are the same size. <br><br>

**Lists** <br>
In contrast, the elements of a list may or may not be next to one another in memory! In this case, knowing the location of the first item in the list does not mean you can simply calculate the location of the other items. <br>
One thing to **Note** is that `Python lists are essentially implemented as arrays`, but also include additional high-level functionality like `append` and `pop` which regular lists in other languages might not have. In particular, the elements of a Python list are contiguous in memory, and they can be accessed using an index. `Python Strings are also Arrays`. They are arrays of bytes representing unicode characters. <br>
To determine the location of list items in memory, `linked-lists` which are discussed later can be used. <br><br>

**Linked-Lists** <br>
Items in a linked list are joined together by? Wait for it **links** 😀. Unlike arrays, you don't know the length of a linked-list. However, you the know the location of the next item you're accessing because of the link. Items are referred to as nodes. <br>
In higher level languages like *Python*, there's no distinction between linked-lists and arrays. While an array typically stores an attribute `index` to tell you the positions of items, a linked list stores the attribute `next` to point to the location of the next item. <br>
It's easier to insert and delete items from a linked list compared to an array. To insert an element between two nodes, 
1. first assign the next value of the new node to the old node on the right,
2. assign the next value of the old node on the left to the new node being inserted, and the insert operation is complete.

Insertion into a linked list takes constant time O(1). To delete, you just change the `next` attribute of the nodes you wish to keep to ignore the unwanted item. **Note:** the next attribute of the last node in a linked-list is *None*, which is how we know which node is last. <br>

You can also have a **Double-Linked-List** data type which has a `next` and `prev` attribute for each node, pointing to their locations in memory. You need to be careful not to lose references to nodes when inserting or deleting from both data types, however, performing these modifications on lists are less comlex than performing them on arrays. <br>

In python linked-lists can be implemented using classes
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)         # Create the first node in the linked-list aka head node
head.next = Node(4)    # Append a new node to the end of the list

print(head.next.value) # Access the value of the second item in the linked-list
4
```

You can also have a **Circular linked-list**. This occur when the chain of nodes links back to itself somewhere. For example `NodeA` -> `NodeB` -> `NodeC` -> `NodeD` -> `NodeB` is a circular list because `NodeD` points back to `NodeB` creating a loop `NodeB` -> `NodeC` -> `NodeD` -> `NodeB`. A circular linked list is typically considered pathological because when you try to iterate through it, you'll never find the end. We usually want to detect if there is a loop in our linked lists to avoid these problems. 
<p align="center">
    <img style="width: 300px; height=120px;" src='figures/two_runners_circular.png'><br>
</p>


### Computational Complexity of Flatenning a Nested Linked List
Lets start with the computational complexity of `merge`.  Merge takes in two lists.  Let's say the lengths of the lists are $N_{1}$ and $N_{2}$. Because we assume the inputs are sorted, `merge` is very efficient. It looks at the first element of each list and adds the smaller one to the returned list.  Every time through the loop we are appending one element to the list, so it will take $N_{1} + N_{2}$ iterations until we have the whole list.<br>

The complexity of `flatten` is a little more complicated to calculate.  Suppose our `NestedLinkedList` has $N$ linked lists and each list's length is represented by $M_{1}, M_{2}, ..., M_{N}$.<br>

We can represent this recursion as:<br>

$merge(M_{1}, merge(M_{2}, merge(..., merge(M_{N-1}, merge(M_{N}, None)))))$ <br>

Let's start from the inside.  The inner most merge returns the $nth$ linked list.  The next merge does $M_{N-1} + M_{N}$ comparisons.  The next merge does $M_{N-2} + M_{N-1} + M_{N}$ comparisons. <br>

Eventually we will do $N$ comparisons on all of the $M_{N}$ elements. We will do $N-1$ comparisons on $M_{N-1}$ elements. <br>

This can be generalized as:<br>

$$
\sum_n^N n*M_{n}
$$
<br>

### Computational Complexity of Sorting a Linked List
Computational complexity is $O(N^2)$ where N is the length of the integer array. One insert is $O(M)$ where $M$ is the length of the existing linked list. As the list grows, the time complexity of inserting grows. It's something like $1 + 2 + 3 + 4 + \cdots + N$.<br>

$$
1 + 2 + 3 + 4 + \cdots + N = \sum_n^N n = \frac{N(N+1)}{2}
$$
<br>

Then our time complexity for sorting itself is $O(N^2)$.  Converting from the linked list to an array is $O(N)$. Combined this is $O(N^2 + N) = O(N^2)$. Sorting algorithms such as quicksort and mergesort (which we'll look at later) are $N \log N$, so this algorithm is slower.<br>

### Swapping Nodes in a LinkedList
### Let's take an example to understand a simple approach - 
Given linked list = [3, 4, 5, 2, 6, 1, 9] <br>
position_one = 2<br>
position_two = 5<br>
**Note the original order of indexes - 0, 1, 2, 3, 4, 5, 6**<br>

**Step 1** - Identify the two nodes to be swapped. Also, identify the previous of both the two nodes. 

<img style="float: center;" src="figures/Step0.png" alt="Linked list showing the two nodes to be swapped, as well as the previous node of each"><br>

**Step 2** - Swap the references making use of a temporary reference
<img style="float: center;" src="figures/Step1.png" alt="The two_previous node is changed to point to the one_current node that it will be swapped with. In this case, the next node of 6 is changed to point to 5 instead of 1"><br><br>
<img style="float: center;" src="figures/Step2.png" alt="Linked list mid-swap showing one link having been updated, and highlighting the temporary reference 2"><br><br>
<img style="float: center;" src="figures/Step3.png" alt="Linked list showing the next node of one_current changing to the next node of two_current instead of the temporary reference. In this case, the next node of 5 points to 9 instead of 2."><br><br>
<img style="float: center;" src="figures/Step4.png" alt="Linked list showing the next node of two_current changing to the temporary reference. In this case, the next node of 1 points to 2 instead of 9."><br><br>
<img style="float: center;" src="figures/Step5.png" alt="Linked list showing the next node of one_previous changing to the node of two_current instead of one_current. In this case, the next node of 4 points to 1 instead of 5."><br><br>
<img style="float: center;" src="figures/Step6.png" alt="Linked list showing the final linked list after swapping two elements."><br>

**Check the order of the updated indexes as - 0, 1, 5, 3, 4, 2, 6**, which implies that index 2 and index 5 have been swapped. 

<br><br>

## Stacks and Queues
 A **stack** is a data structure that consists of two main operations: `push` and `pop`. 
 - A push is when you add an element to the top of the stack and a pop is when you remove an element from the top of the stack.

Stacks can be implemented using arrays or linked lists in python, however, the selected option affects the **time complexity** of stack operations. 
- If we pop or push an element with a linked list stack, there's no traversal. We simply add or remove the item from the head of the linked list, and update the head reference. So with our linked list implementaion, pop and push have a time complexity of **O(1)**.
- If you use arrays, there's a copy overhead that's required each time the array is at capacity. Adding an item to the stack is fine—until we run out of space. Then we would have to create an entirely new (larger) array and copy over all of the references from the old array. *I don't like this because it can create latency overheads for long arrays*. Using a linked list avoids this issue compared to an array implemention of a stack. 
- The copy overhead happens because, with an array, we had to specify some initial size (in other words, we had to set aside a contiguous block of memory in advance). But with a linked list, the nodes do not need to be contiguous. They can be scattered in different locations of memory, an that works just fine. This means that with a linked list, we can simply append as many nodes as we like. Using that as the underlying data structure for our stack means that we never run out of capacity, so pushing and popping items will always have a time complexity of O(1).

<br>

Potential applications of a stack are 
- Implementing a news feed for a web app
- Balancing parentheses in a code editor
- Rearranging text in a string

<br>

Stacks can be easily **reversed** using a time complexity of O(n) and space complexity of O(n). To reverse the stack, 
- create a new stack
- pop items from the old stack while it isn't empty
- push the popped items into the new stack
Because the stack architecture is LIFO, the first item from the old stack is reversed to the bottom of the new stack. This will typically delete all the items in your original stack, hence the Udacity solution implements a recursive call to keep both the original and reversed stacks populated.<br><br>



A **queues** is a data structure that consists of two main operations: enqueue and dequeue. Queues are very similar to stacks but unlike stacks, the follow a FIFO data structure. The first element in is the first element out. When you add an element to the *tail* of the queue, the operation is called **enqueue**. When you remove an element from the *head* of the queue, the operation is called **dequeue**. There's also an operation called **peek**, where y look at the head element but you don't remove it. There are 2 main types of queues namely:
- **Deque**: pronounced *deck*, is a combination of a queue and a stack that allows dequeing or enqueing operations from either the head or tail of the queue. 
- **Priority QUeue**: Each element in the queue has a priority attribute. Whenever a dequeue operation is performed, the element with the highest priority is removed first. If two elements have the same priority, the oldest one is removed first.
<br>

Queues can also be implemented using arrays and linked lists. 
- When using **linked lists**, the Queue class should have a head and tail attribute unlike Stacks that only have a head attribute. When an enqueue operation is performed, the item is added to the **tail**, and when a dequeue operation is performed, the item is added to the **head**. <br>
    When we use enqueue, we simply create a new node and add it to the tail of the list. And when we dequeue an item, we simply get the value from the head of the list and then shift the head variable so that it refers to the next node over. Both of these operations happen in constant time—that is, they have a time-complexity of **`O(1)`**.
- When using **arrays**, issues exist when the array becomes full, and items have to be moved around. The copy overhead also requires a modulu "%" operation to find the position of the `start` and `next_index` attributes within the class. In summary, don't implement queues using an array except when necessary.
- Queues can also be created with **Stacks** that use high level python functions like append and pop. Many of the queue methods can be implemented relatively easily however, the dequeue operation requires you to reverse the list twice, resulting in a `O(n)` complexity, compared to O(1) of a linked list.
- Like Stacks, Queues can also be implemented using python standard list methods like append and pop. The exception when using pop for dequeing a Queue, is to set an index of zero e.g `self.items.pop(0)`
- Queues can also be reversed with a time complexity of O(2n) and a spcae complexity of O(2n).
    - First initialize an empty **stack**
    - **Dequeue** the main Queue and **push** the results into the stack which has a LIFO behaviour
    - Re-**Enqueue** the main queue by **popping** the stacks items into the queue, and the item order will be reversed.
    - Both while operations will require traversing the entire queue.


## Recursion
When you hear the terms *recursion* or *recursive*, this might remind you of the terms *repetition* and *repetitive* — and this is a good connection, because recursion does indeed involve repetition. However, recursion isn't just about repetition. <br>
With recursion, we *solve a problem by first solving smaller instances of the same problem*. In practice, this often involves calling a function from within itself—in other words, we feed some input into the function, and the function produces some output—which we then feed back into the same function. And we continue to do this until we arrive at the solution. <br>
In some regards, you can think of recursive functions as a `while` loop. it keeps calling itself until a termination criteria / exit condition is met. If the termination criteria is not met, you can get stuck in an `infinite recursion loop` where the function keeps calling itself infinitely.
- Properties of a recursive function
    - The function calls itself
    - The function has a base case (This is like the exit condition. Let's the function know when to stop).
    - The function needs to alter the input parameter at some point (similar to updating the variable in a while loop)
- Example of a recursive function
    ```bash
    # Pseudo-code
    function recursive(input) {
        # Define the base case which is the exit conditon
        if input <= 0
            return input  # Function will stop whenever zero is reached
        else
            # Call the function on itself and alter input parameter
            output = recursive(input - 1)
            return output
    }
    ```
    Python implementation of example
    ```python
    def recursive_subtraction(inputs):
        if inputs <= 0:
            return input
        else:
            output = recursive(input - 1) 
            return output
    
    # Call the function. It'll keep running until zero is reached
    recursive_subtraction(5)

    # Analogous to while loop
    inputs = 5
    while inputs != 0:
        inputs -= 1
    ```

Each time you write recursive function, think carefully about the base-case and when you'll like to recursion to stop. If the base-case is improperly defined, you run the risk of falling into a recursion loop. Use `print()` / `console.log()` / `printf()` statements to debug the code where necessary to understand what's happening. <br>

- When using recursion, there are a few things to look out for that you don't have to worry about when running a loop (iteratively). Let's go over a few of those items.
    - **Call stack**: If too many recursive calls are made, an error is encountered `RecursionError: maximum recursion depth exceeded in comparison`. <br>
    Python has a limit on the depth of recursion to prevent a [stack overflow](https://en.wikipedia.org/wiki/Stack_overflow). However, some compilers will turn [tail-recursive functions](https://en.wikipedia.org/wiki/Recursion_(computer_science)#Tail-recursive_functions) into an iterative loop to prevent recursion from using up the stack. Since Python's compiler doesn't do this, you'll have to watch out for this limit.
    - **Slicing**: When slicing arrays, using recursion might not always be efficienct. Look at the `01_recursion_intro` script for additional details. In some cases recursion is more readable and in some cases (loops) iteration is more readable. As you gain experience reading other people’s code, you’ll get an intuition for code readability.

<br><br>

## Trees
Trees are like linked lists however, a single node of a tree can be connected to multiple child nodes. Properties of trees include
- A tree must be completely connected i.e if you're starting  from the root, there must be a way to reach any leaf(node) within the tree.
- There must not be any cycles in the tree. Cycles are like circular linked lists that form loops. It allows you to encounter the same node twice.

### Tree Terminology
A tree can be described in terms of 
- **levels** (how long it will take to reach the root node). The root node is level 1.
- Nodes in a tree are described using parents and children. If a node has multiple children, the children after the first child are siblings.
    - A node can be a parent and a child depending on its level within the tree
- Nodes are the lowest level are called **leaves** or external nodes.
- Parent nodes are also known as internal nodes.
- Connections between 2 nodes are called **edges**, and a   group of connections across multiple nodes are referred to a s **path**.
- The **height** of a node is the distance between the node and the farthest leaf on the tree.
- The **depth** of a node is the number of edges to the `root node`. Height and depth have inverse relationships.

### Tree Traversal
1. **Depth First Search (DFS)** - Explore any children nodes that exist before moving along. 
    1. **Pre-order Travesal** - Start at root -> select the first child node (usually the one on the *left*) -> Continue traversing left nodes until we hit a leaf -> Once a leaf is encountered, go  up on level and *checkoff* the node on the right. Keep checking out nodes till all the nodes   on the left and right of the root have been traversed.
    2. **In-order Traversal** - A node is only checked off when we've seen its left child and come back to it.
    3. **Post-order Traversal** - A node is only checked off when we traversed all its children.
2. **Breadth First Search (BFS)** - Explore all nodes at the same level bbefore moving along
    1. **Level Oreder traversal** - Start at root -> visit all the children at level 2 -> continue to level 3 and visit all the children till you get to the leaves

### 1. Binary Trees
Binary Tress are trees where parents have at **most** 2 children. 
- `Search` and `Delete` operations with a Binary tree is linear with an `O(n)` complexity. 
- Each level can hold nodes up to a power of two making it easier for `insert` operations. Each node has 2 children, so each can have twice as many children as the previous level. This allows insert opeartions to have a complexity of `O(log(n))`
    | Level | Node Capacity |
    | :---: | :-----------: |
    | 1 | 2<sup>0</sup> |
    | 2 | 2<sup>1</sup> |
    | 3 | 2<sup>2</sup> |
    | 4 | 2<sup>3</sup> |

Trees are not inherently organized data structures and rules have to be defined to ensure easier implementation of search, insert, and delete operations.

### 1.1 Binary Search Trees
Binary Search Trees (BST) are a more specific form of Binary Trees. BSTs are **sorted** so that every value on the left side of a node is smaller than the internal node, and every value on the right side is larger than the parent. Like the Binary tree, it's also allowed to have only two children. <br>
When `searching` through a BST, we start at the root node. If the target is *smaller* than the root's value, we go **left**, else if it is *larger*, we go **right**. This allows search operations to be completed in `O(log(n))` time. `Insertion` operations also have  a similar complexity. `Delete` operations are still complicated like regular binary trees so similar considerations apply. <br>
The one drawback of BST is that they can be unbalanced, resulting on nodes occuring only on the right of either the root or an internal node. This lowers the time complexity from O(log(n)) to O(n) because all the nodes are now linear. 