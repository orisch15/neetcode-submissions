class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i not in memo:
                skip = dp(i+1)
                take = dp(i+2) + nums[i]
                memo[i] = max(skip, take)

            return memo[i]
            
        return dp(0)
        