list = [0, 1, 2, 3, 4, 5]

def sum_two(A, target):
	pairs = []
	for i in range(len(A)):
		j = i + 1
		while j < len(A):
			if A[i] + A[j] == target:
				pairs.append("("+ str(A[i]) +", "+str(A[j])+")")
			j += 1
	return pairs

# assuming there is only one solution and the list is sorted
# Time Complexity : O(n)
# Space Complexity : O(1)
def sum_two_one_loop(A, target):
	i = 0
	j = len(A) - 1
	while i < j:
		if A[i] + A[j] == target:
			print(A[i], A[j])
			return True
		elif A[i] + A[j] < target:
			i += 1
		elif A[i] + A[j] > target:
			j -= 1
	return False

# assuming there is only one solution and the list is sorted
# Time Complexity: O(n)
# Space Complexity: O(n)
def sum_two_hash_table(A, target):
	ht = dict()
	for i in range(len(A)):
		if A[i] in ht:
			print(ht[A[i]], A[i])
			return True
		else:
			ht[target - A[i]] = A[i]
	return False

# assuming there is only one solution and the list is sorted
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def sum_two_brute_force(A, target):
	for i in range(0, len(A) - 1):
		for j in range(i + 1, len(A)):
			if A[i] + A[j] == target:
				print(A[i], A[j])
				return True
	return False
