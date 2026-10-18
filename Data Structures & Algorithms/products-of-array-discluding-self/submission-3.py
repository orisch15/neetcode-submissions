class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = set()
        for i in range(len(nums)):            
            if nums[i] != 0:
                product = product*nums[i]
            else:
                zeros.add(i)
        
        zero = (len(zeros) == 1)
        if len(zeros) > 1:
            return [0] * len(nums)

        output = [product] * len(nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                if zero:
                    output[i] = 0
                else:
                    output[i] = output[i] // nums[i]
            else: 
                output[i] = product

        return output

        