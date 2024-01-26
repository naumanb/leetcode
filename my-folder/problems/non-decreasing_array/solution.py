class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        track = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                track += 1
                if i>0 and nums[i-1]>nums[i+1]:
                    nums[i+1] = nums[i]
                if track > 1:
                    return False
        return True
