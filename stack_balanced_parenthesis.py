from stack_data_structure import Stack 

s = Stack()

def is_match(p1, p2):
	if p1 == "{" and p2 == "}":
		return True
	elif p1 == "(" and p2 == ")":
		return True
	elif p1 == "[" and p2 == "]":
		return True
	else:
		return False 


def is_balanced(paren_string):
	index = 0 
	is_balanced = True
	while index < len(paren_string) and is_balanced:
		paren = paren_string[index]
		print(paren)
		if paren in "({[":
			s.push(paren)
		else:
			if s.is_empty(): 
				is_balanced = False
			else:
				top = s.pop()
				if not is_match(top, paren):
					is_balanced = False
		index += 1
	if s.is_empty() and is_balanced:
		return True
	else:
		return False

