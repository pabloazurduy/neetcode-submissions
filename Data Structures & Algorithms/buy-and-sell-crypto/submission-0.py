class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inc = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j]-prices[i]>inc:
                    inc = prices[j]-prices[i]
        return inc