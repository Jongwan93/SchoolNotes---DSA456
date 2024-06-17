#    Main Author(s): 	Steven Hur
#    Main Reviewer(s):	Steven Hur




class SortedList:
	class Node:
		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev

		def get_data(self):
			return self.data

		def get_next(self):
			return self.next

		def get_previous(self):
			return self.prev

	def __init__(self, data = None):
		self.head = None
		self.tail = None
		if data is not None:
			self.head = self.Node(data)
			self.tail = self.head

	def get_front(self):
		return self.head

	def get_back(self):
		return self.tail

	def is_empty(self):
		return self.head is None

	def __len__(self):
		count = 0
		current = self.head
		while current is not None:
			count+=1
			current = current.next
		return count

	def insert(self, data):
		node = self.Node(data)

		if self.is_empty():   # empty linked-list
			self.head = node
			self.tail = node
			return node		
		else:
			if node.data < self.head.data:
				node.next = self.head
				node.prev = self.head.prev
				self.head.prev = node
				self.head = node
				return node
			else:
				current = self.head
				while current is not None:
					if node.data < current.data:
						previous_node = current.prev
						previous_node.next = node
						current.prev = node
						node.next = current
						node.prev = previous_node
						return node
					
					current = current.next
				
				self.tail.next = node	# cannot use current for self.back.next
				node.prev = self.tail
				self.tail = node
				return node
			
	def erase(self, node):
		if node is None:
			raise ValueError('Cannot erase node referred to by None')
		
		if self.head == node:
			if node.next is not None:
				self.head = node.next
				node.next.prev = node.prev
			else:
				self.head = None
				self.tail = None
			del node
		else:
			if node.next is None:
				node.prev.next = None
				self.tail = node.prev
			else:
				node.prev.next = node.next
				node.next.prev = node.prev
			del node				

	def search(self, data):
		current = self.head
		while current is not None:
			if(current.data == data):
				return current
			current = current.next
		return None
			
	def display(self):
		current = self.head
		while current is not None:
			print(current.data)
			current = current.next
			
lst = SortedList()
lst.insert(5)
lst.insert(2)
lst.insert(4)
lst.insert(3)
lst.insert(9)
lst.insert(1)
lst.insert(15)
lst.insert(10)
lst.insert(20)
lst.insert(11)
lst.display()


