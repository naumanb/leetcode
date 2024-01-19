class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charS = {}
        charT = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter in charS:
                charS[letter] += 1
            else:
                charS[letter] = 1
        
        for letter in t:
            if letter in charT:
                charT[letter] += 1
            else:
                charT[letter] = 1

        return charS == charT