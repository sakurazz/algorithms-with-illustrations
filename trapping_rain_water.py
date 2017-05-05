# Time: O(n)
# Space: O(1)
#
# Given n non-negative integers 
# representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

'''
Notes:
Greedy, two pointers
1. find the start point whose next integer becomes smaller
  I
 II
III
2. trap water until we find a bigger integer 
                  I  
                  I  
        I         I         
  I     I         I         I
 IIII  II         I         I    I
IIIIIIIII.........I.........IIIIIII
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == None or len(height) == 0:
            return 0

        max_i = 0
        n = len(height)
        for i in range(1, n):
            if height[i] > height[max_i]:
                max_i = i

        l, r = 0, n - 1
        water = 0

        while l < r and height[l] < height[l + 1]:
            l += 1
        while l < r and height[r] < height[r - 1]:
            r -= 1

        for i in range(l + 1, max_i):
            if height[i] < height[l]:
                water += height[l] - height[i]
            else:
                l = i

        for i in range(r - 1, max_i , -1):
            if height[i] < height[r]:
                water += height[r] - height[i]
            else:
                r = i 

        return water 


if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = Solution().trap(height)
    print(result)  # Output: 6
