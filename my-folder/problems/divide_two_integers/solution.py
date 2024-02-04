class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > INT_MIN:
                return -dividend
            else:
                return INT_MAX
        
        # if dividend XOR divisor < 0
        neg = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            return -dividend if neg else dividend
        
        # loga (x/y) = loga x - loga y
        result = (math.exp(math.log(dividend) - math.log(divisor)))
        result += 0.0000000001
        result = int(result)
        
        return -result if neg else result



