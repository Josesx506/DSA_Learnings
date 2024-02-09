'''
Hash Function for Strings
For a string, say abcde, a very effective function is treating this as number of prime number base p. 
Let's elaborate this statement.

For a number, say 578, we can represent this number in base 10 number system as
            5∗102+7∗101+8∗100
Similarly, we can treat abcde in base p as
            𝑎∗𝑝4+𝑏∗𝑝3+𝑐∗𝑝2+𝑑∗𝑝1+𝑒∗𝑝0
Here, we replace each character with its corresponding ASCII value.

A lot of research goes into figuring out good hash functions and this hash function is one of the most 
popular functions used for strings. We use prime numbers because the provide a good distribution. The 
most common prime numbers used for this function are 31 and 37.

Thus, using this algorithm, we can get a corresponding integer value for each string key and use it as 
an index of an array, say bucket array. It is not a special array. We simply choose to give a special 
name to arrays for this purpose. Each entry in this bucket array is called a bucket and the index in 
which we store a bucket is called bucket index. You can visualize the bucket array as shown in the 
Readme
'''
class HashMap:
    
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37                  # a prime numbers 
        self.num_entries = 0
        
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
    
    # Returns the bucket_index
    def get_bucket_index(self, key):
        return self.get_hash_code(key)  # The returned hash code will be the bucket_index
    
    
    # Returns the hash code
    def get_hash_code(self, key):
        key = str(key)
        
        # represents (self.p^0) which is 1
        current_coefficient = 1         
        
        hash_code = 0
        
        for character in key:
            hash_code += ord(character) * current_coefficient
            current_coefficient *= self.p

        return hash_code                # The generated hash code will be the bucket_index


hash_map = HashMap()
bucket_index1 = hash_map.get_bucket_index("abcd")
bucket_index2 = hash_map.get_bucket_index("bcda")
print(f"|{bucket_index1}| \t -- \t |{bucket_index2}|")


