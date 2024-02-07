class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        

        low, mid, high = 0, 0, len(nums) - 1
        
        if low == high and nums[0] == target:
            return 0

        while low <= high:
            mid = (high+low)//2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]: # if nums[low ... mid] is sorted
                if nums[low] <= target <= nums[mid]: # if target is within range
                    high = mid-1 # move high index to end 1st range
                else:
                    low = mid+1 # move low index to start of 2nd range
            else: # else nums[mid ... high] must be sorted
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1

        return -1