# Matrix


## Best practice 

edge case: [], [[]]

``` python 
if not matrix or not matrix[0]:
	return 0
```


get valid neighbors

``` python 
def neighbors(r, c): 
	for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
	    if 0 <= nr < R and 0 <= nc < C:
	        yield nr, nc
```