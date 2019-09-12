

class Node():
	
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList():
	
	def __init__(self):
		self.head = None

	def append(self, data):
		
		new_node = Node(data)
		if not self.head:
			self.head = new_node
		else:
			last_node = self.head			
			while last_node.next:
				last_node = last_node.next
			last_node.next = new_node
			new_node.prev = last_node

	def prepend(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node()
		else:
			self.head.prev = new_node
			new_node.next = self.head
			self.head = new_node

	def print_list(self):
		current_node = self.head

		while current_node:
			print(current_node.data)
			current_node = current_node.next

	def add_after_node(self, key, data):
		new_node = Node(data)
		current_node = self.head
		while current_node.data != key and current_node:
			current_node = current_node.next
		if current_node.next:
			next_node = current_node.next
			next_node.prev = new_node
			new_node.next = next_node
		current_node.next = new_node 
		new_node.prev = current_node


	def add_before_node(self, key, data):
		new_node = Node(data)
		if key == self.head.data:
			self.head.prev = new_node
			new_node.next = self.head
			self.head = new_node
		current_node = self.head
		previous_node = None
		while current_node.data != key and current_node:
			previous_node = current_node
			current_node = current_node.next
		previous_node.next = new_node
		new_node.prev = previous_node
		new_node.next = current_node
		current_node.prev = new_node 

	def delete_node_by_key(self, key):
		if not self.head:
			print("linked list is empty")
			return
		if self.head.data == key:
			if self.head.next:
				self.head = self.head.next
				self.head.prev = None
				return
			else:
				self.head = None
				return
		current_node = self.head
		previous_node = None
		while current_node and current_node.data != key:
			previous_node = current_node
			current_node = current_node.next
		if current_node.next:
			next_node = current_node.next
			previous_node.next = next_node
			next_node.prev = previous_node
			current_node = None
			return
		previous_node.next = None
		current_node = None
		return

	def delete_node_by_node(self, node):
		if not self.head:
			print("linked list is empty")
			return
		if self.head == node:
			if self.head.next:
				self.head = self.head.next
				self.head.prev = None
				return
			else:
				self.head = None
				return
		current_node = self.head
		previous_node = None
		while current_node and current_node != node:
			previous_node = current_node
			current_node = current_node.next
		if current_node.next:
			next_node = current_node.next
			previous_node.next = next_node
			next_node.prev = previous_node
			current_node = None
			return
		previous_node.next = None
		current_node = None
		return

	def reverse(self):
		current_node = self.head
		last_node = None

		while current_node:
			next_node = None
			if current_node.next:
				next_node = current_node.next
			current_node.next = current_node.prev
			current_node.prev = next_node
			last_node = current_node
			current_node = next_node

		self.head = last_node

	def remove_duplicates(self):
		occurrences = dict()
		current_node = self.head
		while current_node:
			if current_node.data not in occurrences:
				occurrences[current_node.data] = 1
			else:
				self.delete_node_by_node(current_node)
				print(current_node.data)
			current_node = current_node.next

	def pairs_with_sum_v1(self, sum):
		pairs = []
		current_node_1 = self.head
		while current_node_1:
			current_node_2 = self.head
			while current_node_2:
				if current_node_1 == current_node_2:
					current_node_2 = current_node_2.next
					continue
				elif current_node_2.data + current_node_1.data == sum:
					if {current_node_1.data, current_node_2.data} not in pairs:
						pairs.append({current_node_2.data, current_node_1.data})
				current_node_2 = current_node_2.next
			current_node_1 = current_node_1.next
		return pairs

	def pairs_with_sum_v2(self, sum):
		pairs = []
		p = self.head
		while p:
			q = p.next
			while q:
				if p.data + q.data == sum:
					pairs.append("(" + str(p.data) + "," + " " + str(q.data) + ")")
				q = q.next
			p = p.next
		return pairs