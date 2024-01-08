class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        sell= 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                sell = i
            if prices[i] > prices[sell]:
                sell = i
                profit += prices[sell] - prices[buy]
                buy = i
        return profit