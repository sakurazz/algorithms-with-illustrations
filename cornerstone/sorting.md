# Sorting 总结

> Stable: the relative order of elements with the same value is maintained. 
> 
> by [stackoverflow](https://stackoverflow.com/questions/20761396/why-selection-sort-can-be-stable-or-unstable)



|    排序算法    |思路 |  优缺点 | 应用场景| 典型题目 | 备注 | 
| ---------- | --- | ---------- | --- | --- | --- |
| quicksort | xx |runs 0(n**2) time in worst-case | 多数情况 | [sort color](https://leetcode.com/problems/sort-colors/description/) | xx |
| mergesort | xx | stable but not in-place | xx | xx | xx |
| heapsort | xx | in-place but not stable | nearly sorted | xx | xx |
| insertsort | xx | better for short arrays |  e.g. 10 or fewer elements | xx | xx |
| counting sort | xx | O(n)|  e.g. integers in the range [0..255] | xx | xx |

其他: merge/quick/heap/selection/insertion/bubble/counting/radix 

**备注**：

- An in-place sort is one which uses 0(1) space; 
- a **stable** sort is one where entries which are equal appear in their original order.


## 基础知识

1. A well-implemented **quicksort** is usually the best choice for sorting. 
2. Most sorting algorithms are not stable. **Merge sort**, carefully implemented, can be made stable.
3. Most sorting routines are based **on a compare function** that takes two items as input and returns -1 if the first item is smaller them the second item, 0 if they are equal and 1 otherwise. However, it is also possible to use **numerical attributes** directly, e.g., **in radix sort.**
4. **Heaps** can be helpful in sorting problems. Briefly, a max-heap (min-heap) stores keys drawn from an ordered set. It supports 0( log n) inserts and 0(1) time lookup for the maximum (minimum) element; the maximum (minimum) key can be deleted in 0( log n) time. 


![compare](https://i.imgur.com/ZyzWmIG.png)

**稳定性**：排序前后两个相等的数相对位置不变，则算法稳定。

**稳定性得好处**：从一个键上排序，然后再从另一个键上排序，第一个键排序的结果可以为第二个键排序所用。


* 1、堆排序、快速排序、希尔排序、直接选择排序**不是稳定**的排序算法；
* 2、基数排序、冒泡排序、直接插入排序、折半插入排序、归并排序是**稳定**的排序算法。


Sorting problems come in two flavors: 
 
*  (1.) use sorting to **make subsequent steps in an algorithm simpler**, and 
*  (2.) design **a custom sorting routine.** 
  
 For the former, it's fine to use a library sort function, possibly with **a custom comparator**. For the latter, use a data structure like **a BST, heap, or array** indexed by values. [Problems 14.4 and 14.7]
 
The most natural reason to sort is if the inputs have **a natural ordering**, and sorting can be used as a preprocessing step to **speed up searching.** [14.5]

For **specialized input**, e.g., a very small range of values, or a small number of values, it's possible to sort in 0(n) time rather than 0(n log n) time. [Problems 6.1 and 14.7]

It's often the case that sorting can be implemented in **less space** than required by a brute-force approach. [Problem 14.2]



## 典型应用

- subsequent
- a custom sorting routine
- preprocess 

## 最佳实践

- [insertion sort](https://repl.it/@WillWang42/insertion-sort)
- [selection sort](https://repl.it/@WillWang42/selection-sort)
- [quick sort](https://repl.it/@WillWang42/quick-sort) 
- [merge sort](https://repl.it/@WillWang42/merge-sort) 
- counting sort
- custom sort 

### quick sort 

``` python
def quick_sort(nums, head, tail):
  if head < tail:
    split_point = partition(nums, head, tail)
    quick_sort(nums, head, split_point-1)
    quick_sort(nums, split_point+1, tail)
  return nums
    
def partition(nums, head, tail):
  pivot, L, R = head, head + 1, tail 
  while L <= R:
    while L <= R and nums[L] <= nums[pivot]:
      L += 1
    while L <= R and nums[R] >= nums[pivot]:
      R -= 1
    if L <= R:
      nums[L], nums[R] = nums[R], nums[L]

  nums[head], nums[R] = nums[R], nums[head]
  return R 
```
- Try [75](https://leetcode.com/problems/sort-colors/description/)

### merge sort 

``` python
def merge_sort(nums):
  if len(nums) > 1:
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i, j, k = 0, 0, 0
    while i < len(left_half) and j < len(right_half):
      if left_half[i] <= right_half[j]:
        nums[k] = left_half[i]
        i += 1
      else:
        nums[k] = right_half[j]
        j += 1
      k += 1
    nums[k:] = left_half[i:] or right_half[j:]
    
  return nums
```

- Try [148](https://leetcode.com/problems/sort-list/)

### insertion sort 

We consider an application of the **decrease-by-one technique** tosorting an array `A[0..n − 1]`. Following the technique’s idea, we assume that the smaller problem of sorting the array `A[0..n − 2]` has already been solved to give us a sorted array of size `n − 1`: `A[0]≤ . . . ≤ A[n − 2]`. 

How can we take advantage of **this solution to the smaller problem** to get a solution to the original problem by **taking into account the element `A[n − 1]`**?  by [Anany](https://www.amazon.com/Introduction-Design-Analysis-Algorithms-3rd/dp/0132316811)

``` python
def insertion_sort(nums):
  for i, num in enumerate(nums[1:]):
    j = i
    while j >= 0 and nums[j] > num:
      nums[j], nums[j+1] = nums[j+1], nums[j]
      j -=1 
  return nums
```

### custom sort 

``` python
def reorder_log_files(logs: List[str]) -> List[str]:
    def f(log):
        id_, rest = log.split(" ", 1)
        return (0, rest, id_) if rest[0].isalpha() else (1,)

    return sorted(logs, key = f) 
```

- [937](https://leetcode.com/problems/reorder-log-files/), [1029](https://leetcode.com/problems/two-city-scheduling/), [1030](https://leetcode.com/problems/matrix-cells-in-distance-order/)

## 木桩训练

1. [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/description/): 引申：350(Fllow up)
2. [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/) : 逆向思维，从右往左
3. [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/):
4. Rend
5. [57. Insert Interval](https://leetcode.com/problems/insert-interval/description/)
6. [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/description/): sorting == a preprocessing step? Speed up searching!
7. partitioning and sorting an array with many repeated entries 
8. team photo day 1 
9. implement a fast sorting algorithm for lists
10. compute a salary threshold


## Explain

- Leverage the sort function of your languages library. Usually, it will have support for either a custom comparison function.


## Thanks 

- [经典排序算法动画](https://github.com/MisterBooo/Article)
- [Sorting and Colours](https://benmosheron.gitlab.io/blog/2019/01/24/sorting.html): 用颜色可视化主要的排序算法，包含如何实现
- [Sorting Algorithms Visualized](https://imgur.com/gallery/voutF)
