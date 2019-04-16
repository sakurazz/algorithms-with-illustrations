# Heap 


![max heap](https://i.imgur.com/LHCxZOp.gif)


## 基础知识 

Use a heap when all you care about is the **largest** or **smallest** elements, and you do not need to support fast lookup, delete, or search operations for arbitrary elements. [Problem 11.1]

A heap is a good choice when you need to compute the k **largest** or k **smallest** elements in a collection. For the former, use a min-heap, for the latter, use a max-heap. [Problem 11.4]

## 典型应用

- top / lowest k: [347](https://leetcode.com/problems/top-k-frequent-elements/description/)
- shortest path: [787]

## 最佳实践

- min heap
- max heap
- shortest path + Dijkstra


### min heap: benchmark

``` python
import heapq
def find_kth_largest(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

### max heap: keep poping 

``` python
def find_kth_largest(self, nums: 'List[int]', k: 'int') -> 'int':
    heap = [-x for x in nums]
    heapq.heapify(heap)
    for i in range(k):
        result = heapq.heappop(heap)
    return -result 
    
# 	return heapq.nlargest(k, nums)[-1]    
```

## 木桩训练 

- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

## Explain

## Q&A

## Thanks



