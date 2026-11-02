class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #build using k loop
        memo = {}

        def dfs(total):
            if total == 0:
                return 0
            if total in memo:
                return memo[total]

            res = 1e9
            for k in coins:
                if total - k >= 0:
                    res = min(res,1 + dfs(total - k))
            memo[total] = res
            return res

        mincoins = dfs(amount)
        return -1 if mincoins >= 1e9 else mincoins
            

