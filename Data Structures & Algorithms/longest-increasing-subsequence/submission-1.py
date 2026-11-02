class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #we want to save the current index, and the last element of the array
        memo = {}

        def dfs(i, j):
            if i >= len(nums):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]

            LIS = dfs(i + 1, j)

            if j == -1 or nums[i] > nums[j]:
                LIS = max(LIS, 1 + dfs(i+1,i))

            memo[(i,j)] = LIS

            return LIS

        return dfs(0, -1)





