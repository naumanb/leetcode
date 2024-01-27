class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_dist = -1
        prev = -1
        n = len(seats)
        for i in range(n): # traverse through the array from left to right
            if seats[i]: # if there is a person in the seat
                if prev == -1: # if this is the first person
                    max_dist = max(max_dist,i) # set the max distance to the current index
                else: # if this is not the first person
                    max_dist = max(max_dist, (i-prev)//2) # set the max distance to the max of the current distance and the distance between the current index and the previous index
                prev = i # set the previous index to the current index
        return max(max_dist,n-prev-1) # return the max distance, if there is nobody between the last person and the remaining seats

            

                
                