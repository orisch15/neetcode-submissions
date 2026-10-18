class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for i in range(len(nums)):            
            if nums[i] != 0:
                product = product*nums[i]
            else:
                zeros +=1
        
        zero = (zeros == 1)
        if zeros > 1:
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

        