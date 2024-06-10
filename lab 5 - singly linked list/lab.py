# singly linked list

# regular simple node constructor. it can only go forward. no Prev
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def print_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

def print_even(head):
    current = head
    while current is not None:
        if(current.data%2 == 0):
            print(current.data)
        current = current.next

def insert_after(head, value, data):
    current = head
    tmp = Node(data)
    while current is not None:
        if(current.data == value):
            tmp.next = current.next
            current.next = tmp
            break
        current = current.next

def is_palindrome(head):
    current = head
    tmpArray = []
    while current is not None:
        tmpArray.append(current.data)
        current = current.next

    current = head

    while current is not None:
        if(current.data != stack.pop()):
            return False
        current = current.next

    return True
    

head = Node(2)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(1)

print_list(head)
print("-")
print_even(head)
print("-")
insert_after(head, 2, 5)
print_list(head)
print("-")

print()
print("=================================================================================")
#===========================================================================================
print()

def get_max(arr):
    return get_max_helper(arr, 0, arr[0])

def get_max_helper(arr, index, current_max):
    if index == len(arr):
        return current_max

    if arr[index] > current_max:
        current_max = arr[index]

    return get_max_helper(arr, index+1, current_max)

print(get_max([2, 1, 5, 3, 4]))

def reverse_string(s):
    if len(s) == 0:
        return s
    
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("seneca"))

def is_palindrome(s):
    return s == is_palindrome_calculate(s)

def is_palindrome_calculate(s):
    if len(s) == 0:
        return s
    return s[-1] + is_palindrome_calculate(s[:-1])

print(is_palindrome("racecar"))
