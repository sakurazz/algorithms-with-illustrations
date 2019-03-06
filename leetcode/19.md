# 19. Remove Nth Node From End of List



Given a linked list, remove the n-th node from the end of list and return its head.

Example:

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?


## Idea 

- dummy node 
- 保持距离，就能找到位置。“刻舟求剑”

### Edge case 

```
[1,2,3,4,5]
2
[1,2]
1
[1]
1
```

## Code 

``` python 
# Time: O(n) where n = the length of linked list 
# Space: O(1)
# 19. Remove Nth Node From End of List

"""
attention: [1] , 1, so that we need `Dummy Node`
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode("dummy")
        dummy.next = head 
        left, tail = dummy, dummy  
        
        for _ in range(n-1):
            tail = tail.next 
            
        prev = left 
        while tail.next:
            prev = left
            left = left.next
            tail = tail.next 
        
        right = left.next 
        prev.next = right 
        return dummy.next 
```