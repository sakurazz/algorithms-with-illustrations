
# Linked list 


![binary search](https://i.imgur.com/7Wh8Jm3.gif)

![binary search tree](https://i.imgur.com/fGqVYqa.gif)

## Notes

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. 


## key words

- find in sorted xx: 35 

## Corner cases


## Exmaple 

## API  

``` python 
bisect.bisect_left(a, x, lo=0, hi=len(a))
```
The returned insertion point `i` partitions the array a into two halves so that `all(val < x for val in a[lo:i])` for the left side and `all(val >= x for val in a[i:hi])` for the right side.


```python 
bisect.bisect_right(a, x, lo=0, hi=len(a))
bisect.bisect(a, x, lo=0, hi=len(a))
```
Similar to bisect_left(), but returns an insertion point which comes after (to the right of) any existing entries of x in a.

The returned insertion point `i` partitions the array a into two halves so that `all(val <= x for val in a[lo:i])` for the left side and `all(val > x for val in a[i:hi])` for the right side.
