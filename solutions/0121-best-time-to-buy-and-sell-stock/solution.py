class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minprice=prices[0]
        for price in range(len(prices)):
            curprofit=prices[price]-minprice
            maxprofit=max(maxprofit,curprofit)
            minprice=min(minprice,prices[price])
        return maxprofit
