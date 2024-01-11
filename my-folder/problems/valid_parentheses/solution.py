class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {"(":")","[":"]","{":"}"}
        stack = []
        for i in s:
            if i in pairs:
                stack.append(i)
            elif len(stack) == 0 or i != pairs[stack.pop()]:
                return False
        return len(stack) == 0