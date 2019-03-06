# 76. Minimum Window Substring


Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


## Idea

* 统计使用掉的指标，满足指标是一直计算，直达不满足。

## Code

``` python
# Time: O(n) where n = len(s)
# Space: O(m) where m = len(t)
# 76. Minimum Window Substring

"""
 i
"ADOBECODEBANC"
      j

"ABC"
"""

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        shortest = s + s 
        
        head = 0 
        seats = collections.Counter(t)
        count = len(t)
    
        def valid(count):
            return count == 0
        
        def update(tail, head, shortest):
            if tail - head + 1 < len(shortest):
                shortest = s[head:tail+1]
            return shortest 
        
        for tail, char in enumerate(s):
            seats[char] -= 1
            if seats[char] >= 0:
                count -=1 
            while valid(count):        
                shortest = update(tail, head, shortest)  
                
                head_char = s[head]
                seats[head_char] += 1 
                head += 1
                
                if seats[head_char] > 0:
                    count += 1

        if shortest ==  s + s:
            return ""
        
        return shortest ****
```