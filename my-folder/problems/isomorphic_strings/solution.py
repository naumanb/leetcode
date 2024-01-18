class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_hash = {}

        for i in range(len(s)):
            if s[i] in char_hash:
                if char_hash[s[i]] != t[i]:
                    return False
            else:
                if t[i] in char_hash.values():
                    return False
                char_hash[s[i]] = t[i]
        return True