class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        sum = []
        for x in nums:
            i = i+x
            sum.append(i)
        return sum