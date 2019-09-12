
# [1, 2, 9] --> "129"

def increase_by_one_v1(array):
	number = array
	result = []
	carry = 0
	first_digit = number.pop()
	if first_digit + 1 > 9:
		result.append((first_digit + 1) % 10)
		carry = 1
	else:
		result.append(first_digit + 1)
	while number != []:
		digit = number.pop()
		if digit + carry > 9:
			result.append((digit + carry) % 10)
			carry = 1
		else:
			result.append(digit + carry)
			carry = 0
	if carry == 1:
		result.append(carry)
	result = int(''.join(map(str, result[::-1])))
	return result


def increase_by_one_v2(array):
	carry = 0
	if array[-1] == 9:
		array[-1] = 0
		carry = 1
	else:
		array[-1] += 1
		carry = 0
	i = -2
	while -i <= len(array):
		if array[i] == 9:
			array[i] = 0
			carry = 1
		else:
			array[i] = array[i] + carry
			carry = 0
		i -= 1
	if carry == 1:
		tmp = array[0]
		array[0] = 1
		array.append(0)

	return array

[1, 0, 0, 1]
3,2,1

def increase_by_one_v3(A):
	A[-1] += 1
	for i in reversed(range(1, len(A))):
		if A[i] != 10:
			break
		A[i] = 0
		A[i-1] += 1
	if A[0] == 10:
		A[0] = 1
		A.append(0)
	return A

	



