# travelling-salesperson-problem 


![tsp dp](https://i.imgur.com/slovM3J.jpg)

## code 

from  - [How to implement a dynamic programming algorithms to TSP in Python?](https://stackoverflow.com/questions/30114978/how-to-implement-a-dynamic-programming-algorithms-to-tsp-in-python)


``` python 
# Assuming n is given.
A = [[0 for i in range(n)] for j in range(2 ** n)]
```

``` python 
# Check whether some city (1-indexed) is inside subset.
if (1 << (i - 1)) & x:
    print 'city %d is inside subset!' % i

# In particular, checking for city #1 is super-easy:
if x & 1:
    print 'city 1 is inside subset!'

# Iterate over subsets with increasing cardinality:
subsets = range(1, 2 ** n)
for subset in sorted(subsets, key=lambda x: bin(x).count('1')):
    print subset, 
# For n=4 prints "1 2 4 8 3 5 6 9 10 12 7 11 13 14 15"

# Obtain a subset y, which is the same as x, 
# except city #j (1-indexed) is removed:
y = x ^ (1 << (j - 1))  # Note that city #j must be inside x.
```

``` python 
# INFINITY and n are defined somewhere above.
A = [[INFINITY for i in xrange(n)] for j in xrange(2 ** n)]
# Base case (I guess it should read "if S = {1}, then A[S, 1] = 0",
because otherwise S = {0} is not a valid index to A, according to line #1)
A[1][1] = 0
# Iterate over all subsets:
subsets = range(1, 2 ** n)
for subset in sorted(subsets, key=lambda x: bin(x).count('1')):
    if not subset & 1:
        # City #1 is not presented.
        continue
    for j in xrange(2, n + 1):
        if not (1 << (j - 1)) & subset:
            # City #j is not presented.
            continue
        for k in xrange(1, n + 1):
            if k == j or not (1 << (k - 1)) & subset:
                continue
            A[subset][j] = min(A[subset][j], A[subset ^ (1 << (j - 1))][k] + get_dist(j, k))
```

## practice 

- 943. Find the Shortest Superstring
 

## reference 


- [How to implement a dynamic programming algorithms to TSP in Python?](https://stackoverflow.com/questions/30114978/how-to-implement-a-dynamic-programming-algorithms-to-tsp-in-python)
- [4.7 Traveling Salesperson Problem - Dynamic Programming](https://www.youtube.com/watch?v=XaXsJJh-Q5Y)
- [code: step by step](https://repl.it/@WillWang42/tsp-943)