class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxCount = 1
        currCount = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                currCount += 1
                maxCount = max(currCount,maxCount)
            else:
                currCount = 1
        return maxCount