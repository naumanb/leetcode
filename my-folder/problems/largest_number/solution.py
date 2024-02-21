from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """        

        def compare(a, b):
            return int(b+a) - int(a+b)
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(compare))
        return str(int(''.join(nums)))
        