# 275. H-Index II


Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

```
Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
```

**Note:**

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

* This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
* Could you solve it in logarithmic time complexity?

## Idea

* 用封住好的binary_search 方法。

## Code

``` python
# Time: O(logn) where n = len(citations)
# Space: O(1)
# 275. H-Index II

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = citations[::-1]
        if len(citations) == 0:
            return 0
        # citations[:point] : i <= citations[i-1]
        point = self.binary_search(citations, 0, len(citations)-1)
        if citations[point-1] < point:
            point -=1
        return point
    
    def binary_search(self, array, left, right):
        mid =  (left + right) // 2
        while left <= right:
            mid = (left + right) // 2
            if array[mid] >= mid + 1:
                left = mid + 1
            else:
                right = mid - 1
        return mid + 1
        
```