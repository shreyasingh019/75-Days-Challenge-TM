class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 1 : 
            return 0
        min = 10000
        profit = 0
        for x in range(size) :
            if min > prices[x] :
                min = prices[x]
            elif profit < prices[x] - min :
                profit = prices[x] - min
        return profit