# Matrix

## 典型应用

- component: [island 系列](https://leetcode.com/problems/number-of-islands/)
- shortest path: [maze 系列](https://leetcode.com/problems/the-maze/) 
- simulation: [Spiral matrix 系列](https://leetcode.com/problems/spiral-matrix-iii/)
- search: [240 search a 2D matrix](https://leetcode.com/problems/search-a-2d-matrix-ii/)

## 最佳实践 Best practice 

- edge case 
- seen
- neighbors
- component
- shortest path (heap)


### edge case: [], [[]]

``` python 
if not matrix or not matrix[0]:
	return 0
```

### visited / seen

``` python
R = len(matrix)
C = len(matrix[0]) if R else 0 # []
seen = [[False] * C for _ in range(R)]
```

### get valid neighbors

``` python 
R = len(matrix)
C = len(matrix[0]) if R  # [[]]

def neighbor(r, c): 
	for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
	    if 0 <= nr < R and 0 <= nc < C:
	        yield nr, nc

def unseen_neighbor(r, c): 
	for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
	    if 0 <= nr < R and 0 <= nc < C and not seen[nr][nc]:
	        yield nr, nc    
```

### get component 

``` python
# matrix[x][y] == 1
# flipped `1` to `0` after visiting
def dfs(x, y):
	matrix[x][y] = 0 # or `0`
	for i, j in neighbor(x, y):
		if not seen[i][j]: dfs(i, j)
	return 1 
```

### shortest path 



## 木桩训练

- [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
- [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
- [505. The Maze II](https://leetcode.com/problems/the-maze-ii/)
- [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
- [885. Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/)
- [1030. Matrix Cells in Distance Order](https://leetcode.com/problems/matrix-cells-in-distance-order/)
