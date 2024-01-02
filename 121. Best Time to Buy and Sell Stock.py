class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        final_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                final_profit = max(profit, final_profit)
            else:
                l = r
            r += 1
        return final_profit



