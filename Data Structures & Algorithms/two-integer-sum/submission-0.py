class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i

        for i in range(len(nums)):
            delta = target - nums[i] 

            if delta in dic and dic[delta] != i: 
                a = [i,dic[delta]]
                a.sort()
                return a

