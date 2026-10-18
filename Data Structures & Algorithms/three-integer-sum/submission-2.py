class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) <= 2): return []
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tar = -nums[i]
            l, r = i+1, len(nums)-1
            while l<r:
                if nums[l]+nums[r] < tar:
                    l+=1
                    
                elif nums[l]+nums[r] > tar:
                    r-=1
                    
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r-=1
                    #while l<r and nums[r] == nums[r-1]:
                    while l<r and nums[r] == nums[r+1]:
                        r-=1

        return res


        