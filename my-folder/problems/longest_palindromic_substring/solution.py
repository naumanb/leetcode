class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expand(i,j):
            left = i
            right = j
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right-left-1

        ans = [0,0]
        n = len(s)
        for i in range(len(s)):
            oddLength = expand(i,i)
            if oddLength > ans[1] - ans[0] + 1:
                half = oddLength // 2
                ans = [i-half,i+half]
            evenLength = expand(i,i+1)
            if evenLength > ans[1] - ans[0] +1:
                half = (evenLength//2) -1
                ans = [i-half,i+1+half]
        return s[ans[0]:ans[1]+1]

                

        