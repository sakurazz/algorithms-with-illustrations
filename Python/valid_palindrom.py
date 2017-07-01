# Time: O(n)
# Space: O(1)

# Question:
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
# For the purpose of this problem, we define empty string as valid palindrome.
#
'''
Notes:
Edge case: '.,' so that we need to make sure l < r when we add 1 to l
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum(): # Edge case: '.,'
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True 

if __name__ == "__main__":
    s = " ,, ab12321ba"
    result = Solution().isPalindrome(s)
    print(result)  # Expected output: True 
    t = "ab123321ba"
    result2 = Solution().isPalindrome(t)
    print(result2) # True 
    r = ",."
    result3 = Solution().isPalindrome(r)
    print(result3) # True 
