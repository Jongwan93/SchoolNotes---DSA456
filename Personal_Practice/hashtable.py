class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def get_value(self):
        return self.value
    def get_key(self):
        return self.key
    def set_value(self, value):
        self.value = value

class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None]*size
    
    def put(self, key, value):
        hash_value = key % self.size
        node = self.table[hash_value]

        if node is None:
            self.table[hash_value] = Node(key, value)
        else:
            while node.next is not None:
                if node.get_key() == key:
                    node.set_value(value)
                    return
                
                node = node.next

            if node.get_key() == key:
                node.set_value(value)
                return
            
            node.next = Node(key, value)
