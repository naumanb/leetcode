class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0

        for i in range(len(s)):
            number = roman_dict[s[i]]
            total += number
            if i>0 and number > roman_dict[s[i-1]]:
                total -= 2*roman_dict[s[i-1]]
        return total
