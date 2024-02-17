class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        if numerator == 0:
            return '0'
        if denominator == 0:
            return ''
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        integer = str(numerator // denominator)
        numerator %= denominator
        if not numerator:
            return sign + integer
        result = integer + '.'
        table = {numerator: len(result)}
        while numerator:
            numerator *= 10
            result += str(numerator // denominator)
            numerator %= denominator
            if numerator in table:
                result = result[:table[numerator]] + '(' + result[table[numerator]:] + ')'
                break
            table[numerator] = len(result)
        return sign + result