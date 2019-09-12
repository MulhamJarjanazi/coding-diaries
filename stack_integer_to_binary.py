from stack_data_structure import Stack 

def divide_by_2(number):
	s = Stack()
	binary_number = ""
	while number > 0:
		remainder = number % 2
		s.push(remainder)
		number = number // 2

	while not s.is_empty():
		binary_number += str(s.pop())

	return binary_number

