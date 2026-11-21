class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        stack.append(0)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                temp_indx = stack.pop()
                res[temp_indx] = i - temp_indx
            stack.append(i)
        return res
        