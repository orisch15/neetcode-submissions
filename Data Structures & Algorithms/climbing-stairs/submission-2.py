class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i, memo):
            if i == n:
                return 1
            if i > n: 
                return 0
            
            
            if i not in memo:
                memo[i] = dp(i+1, memo) + dp(i+2, memo) 
            return memo[i]

        return dp(0, {})


        