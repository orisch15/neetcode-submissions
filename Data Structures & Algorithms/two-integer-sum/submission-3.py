class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, num in enumerate(nums):
            look = target - num
            if look in numDict:
                return [numDict[look], i]
            numDict[num] = i
        return 0
        

        