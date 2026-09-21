class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for i in prices:
            if i > buy:
                profit = i - buy
                max_profit = max(max_profit, profit)
            if i < buy:
                buy = i
        return max_profit