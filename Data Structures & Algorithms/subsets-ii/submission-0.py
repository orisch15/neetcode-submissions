class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # the loop method
        res = []
        nums.sort()

        def back(start, arr):

            res.append(arr.copy())

            for k in range(start, len(nums)):
# we want to add the repeting number only once so it would be the only branch that starts with it
                if k > start and nums[k] == nums[k - 1]:
                    continue
                arr.append(nums[k])
                back(k + 1, arr)
                arr.pop()
        back(0, [])
        return res