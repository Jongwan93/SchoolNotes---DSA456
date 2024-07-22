# Binary Search Tree

class Node:
    # defining Node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # similar to linkedlist self.head = None
    def __init__(self):
        self.root = None
     
    # T(n) = O(n)
    def insert_node(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
        
        else:
            current = self.root
            parent = None

            while True:
                parent = current
                if value < current.value:
                    # current is updated with current.left to check if left slot is empty
                    current = current.left
                    if current is None:
                        parent.left = node
                        return
                
                # avoid duplicate so no equal value
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        return
    
    # T(n) = O(n)
    def print_nodes(self):
        # create an empty stack
        stack = []
        current = self.root
        # it means while current and stack are not None
        while current or stack:
            # means current is not None
            # anytime you add element in stack, you go left
            if current:
                stack.append(current)
                current = current.left
            # anytime you remove element in stack, you go right
            else:
                current = stack.pop()
                print(current.value, end = ' ')
                current = current.right

    def search_node(self, value):
        current = self.root
        while current:
            if current.value == value:
                return current
            else:
                if value < current.value:
                    current = current.left
                else:
                    current = current.right

        # **Another way**
        # while current and current.value != value:
        #   if value < current.value:
        #       current = current.left
        #   else:
        #       current = current.right
        # return current

tree = BinarySearchTree()
tree.insert_node(5)
tree.insert_node(10)
tree.insert_node(2)
tree.insert_node(11)
tree.insert_node(1)
tree.insert_node(3)
tree.insert_node(20)
tree.insert_node(15)
tree.insert_node(12)
tree.print_nodes()
print("Found" if tree.search_node(4) != None else "Not Found")



#

