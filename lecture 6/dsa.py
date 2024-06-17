# tables
# hashing / hash tables
# called hashing technique

# if you know where the data is, time complexity if O(1)
# collision is major problem of hash table

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def get_value(self):
        return self.value
    def get_key(self):
        return self.key
    def set_value(self, value):
        self.value = value

class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # table is a list/array in python

    def put(self, key, value):
        # hash function
        hash_value = key % self.size
        node = self.table[hash_value] # returns first head node of the linked list

        if node is None:
            self.table[hash_value] = Node(key, value)

        else:
            while node.next is not None:
                # updating existing value of node
                if node.get_key() == key:
                    node.set_value(value)
                    return
                
                node = node.next
            
            # modification of first node when there is only single node
            if node.get_key() == key:
                node.set_value(value)
                return
            
            node.next = Node(key, value)

    def get(self, key):
        hash_value = key % self.size
        node = self.table[hash_value]

        while node is not None:
            if node.get_key() == key:
                return node.get_value()
            node = node.next
        return -1

    def display(self):
        for i in range(self.size):
            node = self.table[i]

            while node is not None:
                print("Key: {}, Value: {}".format(node.get_key(), node.get_value()))
                node = node.next

hashMap = HashMap(10)
hashMap.put(1, 25)
hashMap.put(2, 38)
hashMap.put(3, 45)
hashMap.put(4, 59)
hashMap.put(5, 66)
hashMap.put(6, 94)
hashMap.put(7, 22)
hashMap.display()
print(hashMap.get(8))

# June 17th Monday midterm
# theoretical questions(5) : explain something. definitions
# algorithm and analysis(20) : 5 step analysis. function given and analysis. time complexity. 4 functions.
#                               some code will be given and fill in the empty lines
#                               OR code is given and debug it (10)
# coding(15) : scenario is given and implement the code.
#           ex) insert a node in middle of linked-list
#           1 recursion and 1 linked-list question
# study sortings
# go through lecture notes
# write 5 step analysis
# try linked-list question in leetcode
