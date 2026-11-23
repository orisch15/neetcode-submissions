class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #the binary decesion tree
        res = []
        sub = []
        nums.sort()

        def back(start):
            if start >= len(nums):
                res.append(sub.copy())
                return 
            sub.append(nums[start])
            back(start + 1)
            sub.pop()

#the non taken branch needs to be uniq and not contain the number at all
            while start + 1< len(nums) and nums[start] == nums[start + 1]:
                start += 1
            back(start + 1)
        back(0)
        return res




