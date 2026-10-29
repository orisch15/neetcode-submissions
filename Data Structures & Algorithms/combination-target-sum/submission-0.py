class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(nums) or total > target:
                return 
            
            #case 1: not including i
            dfs(i+1, cur, total)
            #case 2: add i and keep includong it
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            #this pop is extreamly important! without it cur will expload
            cur.pop()

        dfs(0, [], 0)
        return res
