class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seenOnce = 0
        seenTwice = 0

        for num in nums:
            seenOnce = ~seenTwice & (seenOnce ^ num)
            seenTwice = ~seenOnce & (seenTwice ^ num)
        
        return seenOnce