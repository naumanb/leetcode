class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxArea = 0

        while left < right:
            if height[left] >= height[right]:
                area = (right-left)*height[right]
                right -= 1
            else:
                area = (right-left)*height[left]
                left += 1
            maxArea = max(maxArea,area)
        return maxArea