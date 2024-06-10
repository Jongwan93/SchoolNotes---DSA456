# linked list
# Array, you need to specify the size but linked list don't need to specify the size.
# each nodes contain at least one element and one address to the next node. 
# each node is object of node class
# you must start from front of the linked list to start iterating. 
# cannot just jump into a random index of an linked list.
# therefore, linked list is much much slower than array

class LinkedList:
    class Node: # inner-class concept
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev
            
    def __init__(self):
        self.front = None   # beginning of the linked list
        self.back = None    # end of the linked list
    
    def push_front(self, data):
        node = self.Node(data, self.front)

        if self.front is None:  # when linked list is empty
            # self.front = node   # first node
            self.back = node    # first node
        else:
            self.front.prev = node
            # self.front = node # duplicated so putting it outside

        self.front = node

    def display(self):
        current = self.front    # current is set to first node

        while current is not None: # means that current is last node. lastnode.next contains None
            print(current.data)
            current = current.next  # current is pointing in next node

lst = LinkedList()
lst.push_front(2)
lst.push_front(5)
lst.push_front(1)
lst.push_front(3)
lst.push_front(4)

lst.display()

print()
print("===================================================================================================")
#=============================================================================================================
print()

# Sentinel Nodes
# use this to avoid edge case run-time error when pushing node into empty linked list
# linked list will never be empty. it will always hold at least two nodes
# and these two nodes are called Sentinel Nodes
# In this case, self.front and self.back can never be None
# self.front -> first Sentinel
# self.back -> last Sentinel
# frontSentinel.next -> backSentinel.next
# backSentinel.prev -> frontSentinel.prev
# front Sentinel will always be the first Node
# back Sentinel will always be last Node

class LinkedList:
    class Node: # inner-class concept
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev
            
    def __init__(self):
        self.front = self.Node(None)   # beginning of the linked list
        self.back = self.Node(None, None, self.front)    # end of the linked list
        self.front.next = self.back
    
    def push_front(self, data):
        node = self.Node(data, self.front.next, self.front)
        self.front.next.prev = node
        self.front.next = node

    def display(self):
        current = self.front.next    # current is set to first node

        while current is not self.back: # means that current is last node. lastnode.next contains None
            print(current.data)
            current = current.next  # current is pointing in next node

lst = LinkedList()
lst.push_front(2)
lst.push_front(5)
lst.push_front(1)
lst.push_front(3)
lst.push_front(4)

lst.display()





