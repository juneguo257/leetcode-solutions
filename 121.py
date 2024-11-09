class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPriceSoFar = 999999 # over 10^4
        maxProfit = 0
        for price in prices:
            if (price < minPriceSoFar):
                minPriceSoFar = price
            elif (price - minPriceSoFar > maxProfit):
                maxProfit = price - minPriceSoFar
        
        return maxProfit