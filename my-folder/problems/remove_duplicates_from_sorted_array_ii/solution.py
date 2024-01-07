class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        counter = 0
        while i < len(nums):
            if (nums[i] == nums[i-1]) and counter == 1:
                del nums[i]
                i -= 1
            elif (nums[i] == nums[i-1]) and counter == 0:
                counter = 1
            else:
                counter = 0
            i += 1
        

                    