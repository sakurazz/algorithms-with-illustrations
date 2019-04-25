# 159. Longest Substring with At Most Two Distinct Characters


Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

```
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
```

Example 2:

```
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
```

## Idea

1. 经典sliding window题目

### Edge case 

```
"eceba"
"aaaaaaaabbbb"
""
"a"
```

## Code 

``` python 
# Time: O(n) where n = len(s)
# Space: O(k) where k = 2
# 159. Longest Substring with At Most Two Distinct Characters

"""
i 
eceba 
  j
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0
        longest = 0
        seats = collections.defaultdict(int)
        
        def is_valid(seats):
            return len(seats) <= 2
        
        for tail, char in enumerate(s):
            seats[char] += 1
            
            while not is_valid(seats):
                head_char = s[head]
                seats[head_char] -= 1
                
                if seats[head_char] == 0:
                    del seats[head_char]
                head += 1
            
            longest = max(tail - head + 1, longest)
            
        return longest 
```