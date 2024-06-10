#storing object in our linked-list
class Student:
    # constructor initiated
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
    
    # method
    def toString(self):
        return "Name: " + self.name + ", CGPA: " + str(self.cgpa)
    
# creating node class outside of linked-list class(Student)
class Node:
    def __init__(self, student, next=None, prev=None):
        # storing student object in data member variable
        self.data = student
        self.next = next
        self.prev = prev
    
class LinkedList:
    # constructor initiated
    def __init__(self):
        self.front = None
        self.back = None

    def push_front(self, data):
        # create an object of new Node class by calling constructor of this class
        node = Node(data, self.front)

        # checking if self.front is None. if True, Linked-list is empty and this is a first node.
        if self.front is None:
            # self.front = node
            self.back = node
        else:
            self.front.prev = node
            # self.front = node
        self.front = node
    
    def push_back(self, data):
        node = Node(data, None, self.back)

        if self.back is None:
            self.front = node
        else:
            self.back.next = node
        self.back = node

    def pop_front(self):
        if self.front is None:
            print("List is empty")
            return
        # checking if there is only one node in linked-list
        elif self.front == self.back:
            rm = self.front 
            self.front = self.back = None
            del rm
        else:
            rm = self.front
            self.front = self.front.next
            self.front.prev = None
            del rm

    def pop_back(self):
        if self.back is None:
            print("List is empty")
            return
        elif self.back == self.front:
            rm = self.back
            self.back = self.front = None
            del rm
        else:
            rm = self.back
            self.back = self.back.prev
            self.back.next = None
            del rm
    
    # display linked-list starting from first node
    def display_front(self):
        # creating simple pointer pointing at the front node
        current = self.front
        while current is not None:
            print(current.data.toString()) 
            current = current.next

    # display linked-list starting from last
    def display_back(self):
        current = self.back
        while current is not None:
            print(current.data.toString())
            current = current.prev

    def length(self):
        count = 0
        if self.front is None:
            return 0
        else:
            current = self.front
            while current is not None:
                count+=1
                current = current.next
        return count
    
    # return -1 if student not found
    # return index of node if student is found
    def search_by_name(self, name):
        current = self.front
        index = 0
        while current is not None:
            if current.data.name == name:
                return index
            index+=1
            current = current.next
        return -1
    
lstf = LinkedList()
lstf.push_front(Student("John", 3.5))
lstf.push_front(Student("Steve", 3.8))
lstf.push_front(Student("Bill", 3.2))
lstf.display_front()
print("Number of nodes: ", lstf.length())
print("Index of student in list: ", lstf.search_by_name("John"))

# output: 
# Name: Bill, CGPA: 3.2
# Name: Steve, CGPA: 3.8
# Name: John, CGPA: 3.5
# **First in Last out**

print()
lstf.pop_front()
print("After pop_front, display again.")
lstf.display_front()
print("Number of nodes after pop_front: ", lstf.length())

print()
print("---------------------------")

lstb = LinkedList()
lstb.push_back(Student("Jamie", 2.5))
lstb.push_back(Student("Sarah", 2.8))
lstb.push_back(Student("Chris", 1.2))
lstb.display_back()

# output:
# Name: Chris, CGPA: 1.2
# Name: Sarah, CGPA: 2.8
# Name: Jamie, CGPA: 2.5
# **First in Last out**

print()
lstb.pop_back()
print("After pop_back, display again.")
lstb.display_back()




print()
print("===========================================================================================")
#===========================================================================================================
print()
