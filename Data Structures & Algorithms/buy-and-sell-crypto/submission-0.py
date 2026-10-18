class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        best = 0
        for sell in prices[1:]:
            best = max(best, (sell-buy))
            buy = min(buy, sell)

        return best

        