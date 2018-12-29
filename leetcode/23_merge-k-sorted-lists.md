# 23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

## Idea

* [A,B,C,D] -> [A,B] by `A = merge(A,D)` and `B = merge(B,C)`
* 所以问题就变成一个组装问题了。然后单独下一个 merge2list(A, B) 就可以了。

## Code 

### 原始稿

```python 
# Time: O(Nlogk) where k == len(lists)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        
        def merge2list(i, j):
            cur = dummy = ListNode("dummy")
            left, right = lists[i], lists[j]
            
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next
            cur.next = left or right 
            lists[i] = dummy.next
        
        j = len(lists) - 1
        while 0 < j:
            i = 0
            while i < j:
                merge2list(i, j)
                i += 1
                j -= 1
        return lists[0]
```