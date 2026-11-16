class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(r,c):
            if r == m-1 and c == n-1:
                return 1
            elif r > m-1 or c > n-1:
                return 0
            if (r,c) not in memo:
                right = dfs(r, c+1)
                down = dfs(r+1, c)
                memo[(r,c)] = right + down
            
            return memo[(r,c)]
        
        return dfs(0, 0)

        