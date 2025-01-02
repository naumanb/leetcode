class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_index:
                return [num_index[complement],i]

            num_index[num] = i

