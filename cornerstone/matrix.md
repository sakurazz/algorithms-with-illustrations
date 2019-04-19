# Matrix


## Best practice 

### edge case: [], [[]]

``` python 
if not matrix or not matrix[0]:
	return 0
```

### visited 

``` python
R = len(matrix)
C = len(matrix[0]) if m else 0 # []
visited = [[False] * C for _ in range(R)]
```

### get valid neighbors

``` python 
R = len(matrix)
C = len(matrix[0]) if R  # [[]]

def neighbor(r, c): 
	for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
	    if 0 <= nr < R and 0 <= nc < C:
	        yield nr, nc
```

#### get component 

``` python 
def bfs(x, y):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
        grid[x][y] = "0"
        map(bfs,(x-1, x+1, x, x), (y, y, y-1, y+1))
        return 1 
    return 0
``` 

