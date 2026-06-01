class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # TC: O(n * n), SC: O(1)
        if len(prices) < 2:
            return 0

        profit = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = max(profit, prices[j] - prices[i])

        return profit