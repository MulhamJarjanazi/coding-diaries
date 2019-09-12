
def can_reach_end(array):
	A = array
	i = 0
	last_element = len(A) - 1
	furthest_reached = A[0]
	while i <= furthest_reached and furthest_reached < last_element:
		furthest_reached = max(furthest_reached, A[i] + i)
		i += 1
	return furthest_reached >= last_element




