# Time: O(n)
# Space: O(1)

# Question:
# Implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false

'''
Notes:
1. Consider all possible edge cases
s:  p:  -> True
s:a p:  -> False

s: abccdecdf
p: abc*cdf
-> True

s: abccdecdf
p: abc*cde
-> Flase # j >= 0 , (cdf, *cde)

s: abccdecdf
p: abc*cdf**
-> True

'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s 

        m = len(s)
        n = len(p)
        i = j = 0
        x = 0
        y = -1

        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                x = i 
                y = j 
                j += 1
            elif y >= 0:
                i = x + 1
                x += 1
                j = y
            else:
                return False

#?
        if i != m:
            return False 

        while j < n and p[j] == '*':
            j += 1

        return j == n 

if __name__ == "__main__":
    s = "abc"
    p = "abc**"
    result = Solution().isMatch(s,p)
    print(result)  # Output: True


# Dynamic Programming
# Time: O(m*n)
# Space: O(m + n)
'''
Notes:
result[i][j] =
1. if p[j] == '?': R[i-1][j-1] 
2. elif p[j] = '*':  R[i-1][j] or R[i][j-1] 
3. else False
'''

class Solution2(object):
    def isMatch(self, s, p):



