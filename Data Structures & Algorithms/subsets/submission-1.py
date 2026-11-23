class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        

        def back(i, arr):
            res.append(arr.copy())
            for k in range(i, len(nums)):
                arr.append(nums[k])
                back(k + 1, arr)
                arr.pop()

        back(0,[])
        return res
        
        