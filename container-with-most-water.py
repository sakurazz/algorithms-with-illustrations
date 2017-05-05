# Time:  O(n)
# Space: O(1)
#
# Question:
# Given n non-negative integers a1, a2, ..., an, 
# where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of 
# line i is at (i, ai) and (i, 0). Find two lines, 
# which together with x-axis forms a container, 
# such that the container contains the most water.
# 
# Note: You may not slant the container.
"""
Notes: 
Greedy, Always choose the bigger area 
between the new one and the old among n rectangle  
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxArea = 0
        
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maxArea = max(maxArea, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea

if __name__ == "__main__":
    height = [1, 2, 3, 4, 5, 6, 7, 8]
    result = Solution().maxArea(height)
    print(result)  # Expected output: 16