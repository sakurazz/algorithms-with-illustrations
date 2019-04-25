# 274. H-Index


![H-index](https://i.imgur.com/mMJ80as.png)

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

```
Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
```
             
**Note**: If there are several possible values for h, the maximum one is taken as the h-index.



## Idea

* 看图说话

## Code 

### 1. O(nlogn)

```python

# Time: O(nlogn) where n = len(citations)
# Space: O(1)
# 274. H-Index

"""
https://i.imgur.com/mMJ80as.png
"""
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        res = 0
        citations.sort(reverse = True)
        for i, time in enumerate(citations):
            if i+1 <= time:
                res += 1
        return res 
        
```

## 2. O(n)

``` python
# Time: O(n) where n = len(citations)
# Space: O(n)
# 274. H-Index

"""
https://i.imgur.com/mMJ80as.png

[0,1,3,5,6]
"""
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        def counting_sort(citations):
            n = len(citations)
            papers = [0] * (n + 1)
            for _, freq in enumerate(citations):
                papers[min(freq, n)] += 1

            sorted_papers = []
            for i, freq in enumerate(papers):
                for _ in range(freq):
                    sorted_papers.append(i)
            return sorted_papers[::-1]

        citations = counting_sort(citations)
        res = 0 
        for i, time in enumerate(citations):
            if i+1 <= time:
                res += 1
        return res 
```