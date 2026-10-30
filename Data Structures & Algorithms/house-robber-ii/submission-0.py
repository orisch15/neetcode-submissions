class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) == 1:
            return nums[0]
        def dp(i, flag):
            if i >= len(nums) or (i == len(nums) - 1 and flag):
                return 0

            #the last hous
            if (i,flag) not in memo:
                skip = dp(i+1, flag)
                take = dp(i+2, flag) + nums[i]
                memo[(i, flag)] = max(take, skip)

            return memo[(i, flag)]

        return max(dp(0, True), dp(1, False))


        