# show price 
```
input: [1.3, 1.4, 2.5, 3.7]
output: [1, 2, 3, 4]
Explanation:  1.3 + 1.4 + 2.9 + 3.9 = 9.5, round(9.5) = 10
round(1.3) = 1
round(1.4) = 1
round(2.9) = 3
round(3.9) = 4
1 + 1 + 3 + 4 = 9 
9 != 10
Thus, 1.4 -> 2

```

用 bucket 去做这道题。

``` python 
def show_final_price(prices):
	count_end_with = [0] * 10
	left_sum = 0 
	total_sum = 0
	for price in prices:
		left, right = str(i).split(price)
		count_end_with[int(right)] += 1
		left_sum += int(left)
		total_sum += price 
	candidate = total_sum - left_sum
	indicators = {}
	start = 9
	while candidate > 0:
		if count_end_with[start] >= candidate:
			indicators[start] = candidate
			candidate = 0
		else:
			indicators[start] = count_end_with[start]
			candidate -= count_end_with[start]
			start -= 1
	res = [0] * len(prices)
	for i, price in enumerate(prices):
		
	
			
			
		
	
		
```