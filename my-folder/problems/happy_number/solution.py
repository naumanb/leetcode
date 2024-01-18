class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n!= 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))
        return True
