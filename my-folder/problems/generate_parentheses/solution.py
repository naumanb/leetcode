class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if n==0:
            return []

        result = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                result.append(S)
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        backtrack()
        return result



