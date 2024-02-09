'''
Time Complexity and Rehashing

We used arrays to implement our hashmaps because arrays offer 𝑂(1)time complexity for both put and get operations.

Note: In case of arrays, put is simply arr[i] = 5 and get is height = arr[i]


1. Put Operation
    - In the put operation, we first figure out the bucket index. Calculating the hash code to figure out the bucket index 
    takes some time.
    - After that, we go to the bucket index and in the worst case we traverse the linked list to find out if the key is 
    already present or not. This also takes some time.

To analyze the time complexity for any algorithm as a function of the input size n, we first have to determine what our 
input is. In this case, we are putting and getting key-value pairs. So, these entries i.e. key-value pairs are our input. 
Therefore, our n is number of such key-value pair entries.

Note: time complexity is always determined in terms of input size and not the actual amount of work that is being done 
independent of input size. That "independent amount of work" will be constant for every input size so we disregard that.

    - In case of our hash function, the computation time for hash code depends on the size of each string. Compared to number 
    of entries (which we always consider to be very high e.g. in the order of 105) the length of each string can be considered 
    to be very small. Also, most of the strings will be around the same size when compared to this high number of entries. 
    Hence, we can ignore the hash computation time in our analysis of time complexity.
    - Now, the entire time complexity essentialy depends on the linked list traversal. In the worst case, all entries would go 
    to the same bucket index and our linked list at that index would be huge. Therefore, the time complexity in that scenario 
    would be 𝑂(𝑛). However, hash functions are wisely chosen so that this does not happen.
    On average, the distribution of entries is such that if we have n entries and b buckets, then each bucket does not have 
    more than n/b key-value pair entries.

Therefore, because of our choice of hash functions, we can assume that the time complexity is 𝑂(𝑛𝑏). This number which 
determines the load on our bucket array n/b is known as load factor.

Generally, we try to keep our load factor around or less than 0.7. This essentially means that if we have a bucket array 
of size 10, then the number of key-value pair entries will not be more than 7.



What happens when we get more entries and the value of our load factor crosses 0.7?
In that scenario, we must increase the size of our bucket array. Also, we must recalculate the bucket index for each entry 
in the hash map.

Note: the hash code for each key present in the bucket array would still be the same. However, because of the compression 
function, the bucket index will change.

Therefore, we need to rehash all the entries in our hash map. This is known as Rehashing.


2. Get and Delete operation
Can you figure out the time complexity for get and delete operation?

Answer: The solution follows the same logic. We assume a constant time of operation for generating the hash code (bucket-index) 
for a given key. Ignore this constant time. Similarly, we can refer to the head of linked list at generated bucket-index in 
O(1) time. Next, we might have to traverse the the linked list in the worst-case scenario, making the time complexity as 𝑂(𝑛𝑏). 
Note that we do not reduce the size of bucket array in delete operation.



Practical Consideration for Time Complexity of put and get Operation
Note: Theoretically, the worst case time complexity of put and get operations of a HashMap can be  𝑂(𝑛𝑏)≈𝑂(𝑛), when  𝑏<<𝑛. 
However, our hashing functions are sophisticated enough that in real-life we easily avoid collisions and never hit O(n). 
Rather, for the most part, we can safely assume that the time complexity of put and get operations will be O(1).

Therefore, when you are asked to solve any practice problem involving HashMaps, assume the worst case time complexity for put 
and get operations to be O(1).
'''
class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    
    def __init__(self, initial_size = 15):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        self.load_factor = 0.7
        
    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
        
        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()
        
    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient
        return hash_code % num_buckets                                # one last compression before returning
    
    def size(self):
        return self.num_entries

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)         # we can use our put() method to rehash
                head = head.next

    
    # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's view the hash map:"

        node = self.bucket_array
        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next
                    
        return output


# Test Rehashing

# We have reduced the size of the hashmap array to increase the load factor (> 0.7) 
# and hence trigger the rehash() function
hash_map = HashMap(5)                        

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))

print(hash_map)                          # call to the helper function to see the hashmap