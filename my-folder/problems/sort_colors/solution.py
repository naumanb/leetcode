class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Using the Dutch National Flag Algorithm

        low = 0
        high = len(nums) - 1
        current = 0

        while current <= high:
            if nums[current] == 0:
                nums[low], nums[current] = nums[current], nums[low]
                low += 1
                current += 1
            elif nums[current] == 1:
                current += 1
            elif nums[current] == 2:
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1
            


    
    

    
        