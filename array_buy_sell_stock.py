arr = [310, 300, 290, 280, 320, 350, 335, 290, 300]


def buy_and_sell_once_v1(A):
	best_price = 0
	best_buy = 0
	best_sell = 0
	i = 0
	for i in range(0, len(A) - 1):
		for j in range(i + 1,len(A)):
			if A[j] - A[i] > best_price:
				best_buy = A[i]
				buy_day = i
				best_sell = A[j]
				sell_day = j
				best_price = A[j] - A[i]
	return "best buy",best_buy,"day",buy_day,"best_sell",best_sell,"day",sell_day

# Time Complexity : O(n^2)
# Space Complexity : O(1)
def buy_and_sell_once_v2(A):
	max_profit = 0
	for i in range(0, len(A)-1):
		for j in range(i + 1, len(A)):
			if A[j] - A[i] > max_profit:
				max_profit = A[j] - A[i]
	return max_profit

# Time Complexity : O(n)
# Space Complexity : O(1)
def buy_and_sell_once_v3(A):
	max_profit = 0
	min_price = A[0]
	for price in A:
		min_price = min(price, min_price)
		compare_profit = price - min_price
		max_profit = max(compare_profit, max_profit)
	return max_profit
