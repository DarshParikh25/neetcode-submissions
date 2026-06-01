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

        i = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                for j in range(i + 1, len(prices)):
                    if prices[j] <= prices[i]:
                        break
                    else:
                        profit = max(profit, prices[j] - prices[i])

        return profit