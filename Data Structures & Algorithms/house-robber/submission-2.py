class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, res):
            if i >= len(nums):
                return res

            if (i + 1, res) not in memo:
                memo[(i + 1, res)] = dp(i+1, res)

            if (i + 2, res + nums[i]) not in memo:
                memo[(i + 2, res + nums[i])] = dp(i+2, res + nums[i])

            skip = memo[(i + 1, res)]
            take = memo[(i + 2, res + nums[i])]

            return max(skip, take)
            
        return dp(0, 0)