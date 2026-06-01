class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        # TC: O(n * n), SC: O(1)
        # profit = 0

        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])

        # return profit

        # TC: O(n), SC: O(1)
        profit = 0
        min_buy = prices[0]

        for price in prices:
            min_buy = min(min_buy, price)
            profit = max(profit, price - min_buy)

        return profit