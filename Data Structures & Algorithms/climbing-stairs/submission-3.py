class Solution:
    def climbStairs(self, n: int) -> int:

        def dp(i, memo):
            if i <= 2:
                return i
            if i not in memo:
                memo[i] = dp(i-1, memo) + dp(i-2, memo) 
            
            return memo[i]

        return dp(n, {})
        