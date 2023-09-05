class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=float("inf")
        maxprofit=float("-inf")
        for price in prices:
            minprice=min(minprice,price)
            maxprofit=max(maxprofit,(price-minprice))
        return maxprofit
        