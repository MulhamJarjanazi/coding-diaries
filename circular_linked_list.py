class Node():
	def __init__(self, data):
		self.next = None
		self.data = data

class CircularLinkedList():
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			self.head.next = self.head
		else:
			current_node = self.head
			while current_node.next != self.head:
				current_node = current_node.next
			current_node.next = new_node
			new_node.next = self.head

	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		current_node = self.head

		if not self.head:
			new_node.next = new_node
		else:
			while current_node.next != self.head:
				current_node = current_node.next

			current_node.next = new_node
		
		self.head = new_node

	def print_list(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next
			if current_node == self.head:
				break
		
	def remove(self, key):
		previous_node = None
		current_node = self.head
		last_node = self.head
		
		while last_node.next != self.head:
			last_node = last_node.next

		while current_node and current_node.data != key:
			previous_node = current_node
			current_node = current_node.next
			if current_node.next == self.head and current_node.data != key:
				print("node doesn't exist!")
				return

		if current_node == self.head:
			if current_node.next != self.head:
				last_node.next = current_node.next
				self.head = last_node.next
			else: 
				self.head = None
			return


		previous_node.next = current_node.next
		current_node = None 


	def get_length_recursive(self, node):
		if not self.head:
			return 0
		if node.next == self.head:
			return 1
		else:
			return 1 + self.get_length_recursive(node.next)



	def split_list(self):
		list_1 = CircularLinkedList()
		list_2 = CircularLinkedList()

		length = self.get_length_recursive(self.head)
		mid_position = length//2 + 1
		count = 1
		current_node = self.head

		while count != mid_position:
			list_1.append(current_node.data)
			current_node = current_node.next
			count += 1

		while current_node:
			if current_node == self.head:
				break
			list_2.append(current_node.data)
			current_node = current_node.next

		return list_1, list_2

# 1 -> *2 -> 3 -> *4 -> 1 -> *2 -> *3 -> *4 -> 1 -> *2 -> *3 -> *4
# 1 -> 3 -> 4
# 1 -> 3
# 1
# 1 -> 2 -> *3 -> *4 -> 1 -> 2 -> 3 -> *4 -> *1 -> 2 -> 3 -> *4
	def josephus_circle(self, step):
		current_node = self.head
		deleted = []
		not_deleted = []
		
		while current_node:
			if current_node.next == self.head:
				not_deleted.append(current_node)
				break
			not_deleted.append(current_node)
			current_node = current_node.next

		current_node = self.head
		count = 1
		while len(not_deleted) != 1:
			if current_node not in deleted:
				if count == step:
					not_deleted.remove(current_node)
					deleted.append(current_node)
					count = 1
				else:
					count += 1
			
			current_node = current_node.next

		return not_deleted[0].data

	def is_linked_list(self , list_):
		last_node = list_.head

		while last_node.next:
			if last_node.next == list_.head:
				return True
			last_node = last_node.next
		return False

	