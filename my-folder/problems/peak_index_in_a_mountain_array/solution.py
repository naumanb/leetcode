class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr)-1
        while left < right: # While the left index is less than the right index
            mid = (left+right)//2 # Calculate the mid index
            if arr[mid] < arr[mid+1]: # if the value at the mid index is less than the value at the next index
                left = mid+1 # set the left index to the next index
            else:
                right = mid # set the right index to the mid index
        return left # return the left pointer as the peak index
