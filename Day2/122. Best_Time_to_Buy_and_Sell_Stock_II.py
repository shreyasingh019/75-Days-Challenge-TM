class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=[0]*(n+1)
        a=prices[::-1]
        if n==1:
            return 0
        if n==2:
            if prices[0]>prices[1]:
                return 0
            else:
                return (prices[1]-prices[0])

        for i in range(1,n):
            profit[i]=profit[i-1]+max(profit[i],a[i-1]-a[i])
     

                
        return profit[n-1]