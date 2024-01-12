class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Indices tracker for the arrays
        j = m-1
        k = n-1
        # starting from the end of the nums1 array
        for i in range(m+n-1,-1,-1):
            if k<0: # if nums2 is empty or has been consumed, leave nums1 as is
                continue
            elif j<0: # if num1 is empty or has been consumed, fill rest of nums1 with nums 2
                nums1[i] = nums2[k]
                k -= 1 # decrement nums2 index
            else: # if both nums1 and nums2 are not empty
                if nums1[j] >= nums2[k]: 
                    nums1[i] = nums1[j] 
                    j -= 1
                else: 
                    nums1[i] = nums2[k]
                    k -= 1
            