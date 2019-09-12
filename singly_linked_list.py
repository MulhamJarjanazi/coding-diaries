class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = Node(None)

	def print_list(self):
		current_node = self.head
		while current_node:
			print(current_node.data)
			current_node = current_node.next

	def append(self, data):
		new_node = Node(data)
		if self.head.data == None:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self, previous_node, data):
		new_node = Node(data)
		new_node.next = previous_node.next
		previous_node.next = new_node

	def delete_node(self, key):
		if key == self.head.data:
			new_head = self.head.next
			self.head.next = None
			self.head = new_head
			return
		previous_node = None
		current_node = self.head
		while current_node and current_node.data != key:
			previous_node = current_node
			current_node = current_node.next
		if current_node == None:
			print("node don't exist!")
			return
		previous_node.next = current_node.next
		current_node = None
		return

	def delete_node_by_position(self, position):
		if position == 0:
			self.delete_node(self.head.data)
			return
		count = 1
		previous_node = None
		current_node = self.head.next
		while current_node and count != position:
			previous_node = current_node
			current_node = current_node.next
			count += 1
		if current_node == None:
			print("postion out of range!")
			return
		previous_node.next = current_node.next
		current_node = None
		return

	def get_length_iterative(self):
		count = 0 
		current_node = self.head
		while current_node:
			count += 1
			current_node = current_node.next
		return count

	def get_length_recursive(self, node):
		if node == None:
			return 0
		return 1 + self.get_length_recursive(node.next)

	
	def swap_nodes(self, key_1, key_2):
		if key_1 == key_2:
			return
		previous_1 = None
		previous_2 = None
		node_1 = self.head
		node_2 = self.head

		while node_1 and node_1.data != key_1:
			previous_1 = node_1
			node_1 = node_1.next
		while node_2 and node_2.data != key_2:
			previous_2 = node_2
			node_2 = node_2.next

		if not node_1 or not node_2:
			return

		if previous_1:
			previous_1.next = node_2
		else:
			self.head = node_2
			previous_2.next = node_1
		if previous_2:
			previous_2.next = node_1
		else:
			self.head = node_1
			previous_1.next = node_2
		node_1.next, node_2.next = node_2.next, node_1.next
		return

	def reverse(self):
		current_node = self.head
		nodes = []
		nodes.append(current_node)
		while current_node.next:
			current_node = current_node.next
			nodes.append(current_node)
		self.head = nodes.pop()
		current_node = self.head
		while nodes != []:
			current_node.next = Node(None)
			current_node.next.data = nodes.pop().data
			current_node = current_node.next
		return

	def reverse_iterative(self):
		previous_node = None
		current_node = self.head
		while current_node:
			nxt = current_node.next
			current_node.next = previous_node
			previous_node = current_node
			current_node = nxt
		self.head = previous_node
		return

	def reverse_recursive(self):
		def _reverse_recursive(current_node, previous_node):
			if not current_node:
				return previous_node
			nxt = current_node.next
			current_node.next = previous_node
			previous_node = current_node
			current_node = nxt
			return _reverse_recursive(current_node, previous_node)

		self.head = _reverse_recursive(current_node = self.head, previous_node = None)
		return
	
	def get_values(self):
		values = []
		current_node = self.head
		while current_node:
			values.append(current_node.data)
			current_node = current_node.next
		return values

	def get_position(self, key):
		index = 0 
		current_node = self.head
		while current_node and key != current_node.data:
			index += 1
			current_node = current_node.next
		if not current_node:
			print("node doesn't exist!")
			return
		return index

	def merge_sorted(self, list_2):
		for value in list_2.get_values():	
			current_node = self.head
			previous_node = None	
			while current_node and value < current_node.data:
				previous_node = current_node
				current_node = current_node.next
			while current_node and value > current_node.data:
				previous_node = current_node
				current_node = current_node.next
			self.insert_after_node(previous_node, value)
		return

	def merge_sorted_v2(self, list_2):
		s = None
		p = self.head
		q = list_2.head

		if not p:
			return q
		if not q:
			return p 
		
		if p.data >= q.data:
			s = q
			q = s.next
			self.head = s
			s.next = p
		

		if q.data >= p.data:
			s = p
			p = s.next
			self.head = s
			s.next = q
			

		while p and s:
			if p.data >= q.data:
				s = q
				q = s.next
				s.next = p
			if q.data >= p.data:
				s = p
				p = s.next
				s.next = q
		
		if not p:
			s.next = q
		if not q:
			s.next = p 
			

	def remove_duplicates(self):
		current_node_1 = self.head
		while current_node_1:
			previous_node_2 = current_node_1
			current_node_2 = current_node_1.next
			
			while current_node_2:
				if current_node_2.data == current_node_1.data:
					previous_node_2.next = current_node_2.next
				
				previous_node_2 = current_node_2
				current_node_2 = current_node_2.next
			
			current_node_1 = current_node_1.next
		
		return 
			  
	def remove_duplicates_v2(self):
		current_node = self.head
		previous_node = None
		duplicate_values = dict()
		while current_node:
			if current_node.data in duplicate_values:
				previous_node.next = current_node.next
				current_node = None
			else:
				duplicate_values[current_node.data] = 1
				previous_node = current_node
			current_node = previous_node.next	 

# Runtime Complexity = O(m) where m = size of the linked list.
	def Nth_to_last(self, N):
		current_node = self.head
		nodes = []
		
		while current_node:
			nodes.append(current_node)
			current_node = current_node.next

		return nodes[-1-N]

# Runtime Complexity = O(n) where n = nth node
	def Nth_to_last_v2(self, N):
		current_node = self.head
		total_length = self.get_length_iterative()
		
		while current_node:
			if total_length == N:
				return current_node
			else:
				total_length -= 1
				current_node = current_node.next
		if not current_node:
			return

# Runtime Complexity = O(n) where n = nth node
	def Nth_to_last_v3(self, N):
		p = self.head
		q = self.head
		count = 0
		while q and count < N:
			q = q.next
			count += 1

		if not q:
			print(str(N)+ " is longer than the list")
			return

		while q:
			p = p.next
			q = q.next

		return p 

	def count_all_occurences(self):
		values = dict()
		current_node = self.head
		while current_node:
			if current_node.data in values:
				values[current_node.data] += 1
			else:
				values[current_node.data] = 1
			current_node = current_node.next
		return values

	def count_occurences(self, data):
		occurences = self.count_all_occurences()
		return occurences[data]

	def count_occurences_iterative(self, data):
		count = 0
		current_node = self.head

		while current_node:
			if current_node.data == data:
				count += 1
			current_node = current_node.next
		return count

	def count_occurences_recursive(self, node, data):
		if not node:
			return 0
		if node.data == data:
			return 1 + self.count_occurences_recursive(node.next, data)
		else:
			return self.count_occurences_recursive(node.next, data)


	

# 1 -> 2 -> 3 -> 4(pivot) -> 5 -> 6 -> 7
# 7 -> 6 -> 5 -> 1 -> 2 -> 3 -> 4
# takes a node as an argument
	def rotate_v1(self, pivot):
		next_node = pivot.next
		
		while next_node:
			next_ = next_node.next
			next_node.next = self.head
			self.head = next_node
			next_node = next_
		
		pivot.next = None
		return

# 1 -> 2 -> 3 -> 4(pivot) -> 5 -> 6 -> 7
# 5 -> 6 -> 7 -> 1 -> 2 -> 3 -> 4
# takes a node as an argument
	def rotate_v2(self, pivot):
		last_node = pivot.next
		
		while last_node.next:
			last_node = last_node.next

		last_node.next = self.head
		self.head = pivot.next
		pivot.next = None
		return

# 1 -> 2 -> 3 -> 4(pivot) -> 5 -> 6 -> 7
# 5 -> 6 -> 7 -> 1 -> 2 -> 3 -> 4
# takes a key as an argument
	def rotate_v3(self, key):
		p = self.head
		q = self.head
		
		while p and p.data != key:
			p = p.next

		while q.next:
			q = q.next

		q.next = self.head
		self.head = p.next
		p.next = None
		return

# 1 -> 2 -> 3 -> 4(pivot) -> 5 -> 6 -> 7
# 5 -> 6 -> 7 -> 1 -> 2 -> 3 -> 4
# takes the position of the pivot node as an argument
	def rotate_v4(self, k):
		p = self.head
		q = self.head
		previous_node = None
		count = 0

		while p and count < k:
			previous_node = p
			p = p.next
			q = q.next
			count += 1
		p = previous_node

		while q:
			previous_node = q
			q = q.next
		q = previous_node

		q.next = self.head
		self.head = p.next
		p.next = None

		return
# RADAR = R -> A -> D -> A -> R
	def is_palindrome(self):
		values_1 = []
		values_2 = []
		
		current_node = self.head
		while current_node:
			values_1.append(current_node.data)
			current_node = current_node.next
		word_1 = ''.join(values_1)
		
		while values_1 != []:
			values_2.append(values_1.pop())
		word_2 = ''.join(values_2)

		return word_1 == word_2

	def is_palindrome_v2(self):
		content = []
		current_node = self.head

		while current_node:
			content.append(current_node.data)
			current_node = current_node.next
		return content == content[::-1]

	def is_palindrome_v3(self):
		content = ''
		current_node = self.head

		while current_node:
			content = content + str(current_node.data)
			current_node = current_node.next
		return content == content[::-1]

	def is_palindrome_v4(self):
		content = []
		current_node = self.head
		while current_node:
			content.append(current_node.data)
			current_node = current_node.next

		current_node = self.head
		while current_node:
			data = content.pop()
			if data != current_node.data:
				return False
			current_node = current_node.next
		return True

	def is_palindrome_v5(self):
		p = self.head
		q = self.head
		previous_nodes = []

		while q:
			previous_nodes.append(q)
			q = q.next
		last_node = None
		while p and p != last_node:
			last_node = previous_nodes.pop()
			if p.data != last_node.data:
				return False
			p = p.next
		return True

	def is_palindrome_v6(self):
		previous_nodes = []
		q = self.head
		p = self.head
		i = 0

		while q:
			previous_nodes.append(q)
			q = q.next
			i += 1

		q = previous_nodes[i-1]
		count = 1
		while count <= i//2 + 1:
			if p.data != previous_nodes[-count].data:
				return False
			p = p.next
			count += 1
		return True 

	def move_tail_to_head(self):
		last_node = self.head
		previous_node = None
		
		while last_node.next:
			previous_node = last_node
			last_node = last_node.next

		last_node.next = self.head
		self.head = last_node
		previous_node.next = None

		return

# hardcore edition xD 
	def sum_two_lists(self, list_2):
		current_node_1 = self.head
		current_node_2 = list_2.head
		numbers_1 = []
		numbers_2 = []
		sum_ = []

		while current_node_1:
			numbers_1.append(current_node_1.data)
			current_node_1 = current_node_1.next

		while current_node_2:
			numbers_2.append(current_node_2.data)
			current_node_2 = current_node_2.next

		count = 0

		while count < len(numbers_1) and count < len(numbers_2):
			each_sum = numbers_1[count]*(10**count) + numbers_2[count]*(10**count)
			sum_.append(each_sum)
			count += 1
		if count == len(numbers_1):
			while count < len(numbers_2):
				sum_.append(numbers_2[count]*(10**count))
				count += 1
		if count == len(numbers_2):
			while count < len(numbers_1):
				sum_.append(numbers_1[count]*(10**count))
				count += 1

		final_sum = 0
		for item in sum_:
			final_sum += item
		sum_list = LinkedList()
		for item in str(final_sum)[::-1]:
			sum_list.append(int(item))

		return sum_list

# primary school summation technique, version 1
	def sum_two_lists_v2(self, list_2):
		current_node_1 = self.head
		current_node_2 = list_2.head
		sum_list = LinkedList()
		carry = 0
		
		while current_node_1 and current_node_2:
			each_sum = current_node_1.data + current_node_2.data + carry
			if each_sum > 9:
				carry = 1
				sum_list.append(each_sum - 10)
			else:
				carry = 0
				sum_list.append(each_sum)
			current_node_1 = current_node_1.next
			current_node_2 = current_node_2.next

		if not current_node_1 and current_node_2:
			if carry == 1:
				sum_list.append(current_node_2.data + 1)
				current_node_2 = current_node_2.next
			while(current_node_2):
				sum_list.append(current_node_2.data)
				current_node_2 = current_node_2.next

		if not current_node_2 and current_node_1:
			if carry == 1:
				sum_list.append(current_node_1.data + 1)
				current_node_1 = current_node_1.next
			while(current_node_1):
				sum_list.append(current_node_1.data)
				current_node_1 = current_node_1.next

		if carry == 1:
			sum_list.append(carry)

		return sum_list

# primary school summation technique, version 2
	def sum_two_lists_v3(self, list_2):
		p = self.head
		q = list_2.head
		sum_list = LinkedList()
		carry = 0

		while p or q:
			if not p:
				i = 0
			else:
				i = p.data
			if not q:
				j = 0
			else:
				j = q.data
			if i+j+carry > 9:
				sum_list.append(i+j-10+carry)
				carry = 1
			else:
				sum_list.append(i+j+carry)
				carry = 0
			if p:
				p = p.next
			if q:
				q = q.next
		if carry == 1:
			sum_list.append(carry)

		return sum_list