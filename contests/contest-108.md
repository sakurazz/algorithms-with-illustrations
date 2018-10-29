# Leetcode contest 108

- [ ] 补集的概念
- [ ] 如何数subarray? start with or end with 
- [ ] 

## 929. Unique Email Addresses

```
Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
```

``` python 
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def clean(email):
            # deal with + .
            left, right = email.split("@")
            first = left.split("+")[0]
            left = first.replace(".", "")
            cleaned = left + right 
            return cleaned
        
        res = set()
        for email in emails:
            new = clean(email)
            res.add(new)
        
        return len(res)
```

## 930. Binary Subarrays With Sum

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

```
Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
```

```python 
"""
s = 3
      
0,0,1,1,0,0,1,1

3*3 + 1 + 3 * 1 = 9 + 1 + 3 = 

0,0,1,1
0,0,1,1,0
0,0,1,1,0,0
  0,1,1
  0,1,1,0
  0,1,1,0,0
    1,1
    1,1,0
    1,1,0,0

0,0,x,0,0
3*3  
  

1,0,1,0,1

x,0 1*2
0,x 2*1

        s             
0,0,0,1,0,1,0,0,0,1,0,1,0,0,0
                      e

  
0,1,0

1,2,3
1,
1,2
1,2,3
3 + 2 + 1
1 + n)


"""

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        def cal(n):
            return (1 + n) * n / 2
        
        n = len(A)
                        
        start = 0
        temp = 0
        res = 0 
        end = 0
        
        if sum(A) < S:
            return 0
        if S == 0:
            if sum(A) == 0:
                return cal(n)
            else:
                zero = 0
                for i, num in enumerate(A):
                    if num == 0:
                        zero += 1
                    else:
                        res += cal(zero)
                        zero = 0
                return res + cal(zero)
                
            
        while end < len(A):
            temp += A[end] 
            while temp > S:
                temp -= A[start]
                start += 1
            if temp == S:
                left, right = 0, 0
                end += 1
                while end < len(A) and A[end] == 0:
                    end += 1
                    right += 1
                while start < end and A[start] == 0:
                    start += 1
                    left += 1
                res += (left + 1) * (right+1)
            else:
                end += 1
        return res 
```

## 931. Minimum Falling Path Sum

Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.
```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
```

```
'''
1, 2, 3
4, 5, 6
7, 8, 9 

1, 2, 3

for x in (j-1), j, (j+1)
dp[i][j] = min(dp[i-1][x]+A[i][j], dp[i][j])

''' python 
class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        dp[0] = A[0]
        for i in range(1, n):
            for j in range(n):
                for k in (j-1, j, j+1):
                    if 0 <= k < n:
                        dp[i][j] = min(dp[i-1][k] + A[i][j], dp[i][j])
        return min(dp[-1])
```

## 932. Beautiful Array

For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)

### 启发：

n-1 -> n
n/2 -> n 

```
Input: 5
Output: [3,1,2,5,4]
```
``` python 
```

