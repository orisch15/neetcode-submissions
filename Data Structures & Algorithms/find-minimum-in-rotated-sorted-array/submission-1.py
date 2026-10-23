class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                #dont forget to add 1 to prevent infanate loop
                l = m + 1
            else:
                r = m
        return nums[l]      