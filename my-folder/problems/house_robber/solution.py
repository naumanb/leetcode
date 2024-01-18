class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1 = 0
        prev2 = 0
        for i in nums:
            temp = prev1
            prev1 = max(prev2 + i, prev1)
            prev2 = temp
        return prev1
            