class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i,j) not in memo:
                if text1[i] == text2[j]:
                    memo[(i, j)] = 1 + dfs(i + 1, j + 1)
                else: 
                    advance_1 = dfs(i + 1, j)
                    advance_2 = dfs(i, j + 1)
                    memo[(i, j)] = max(advance_1, advance_2)

            return memo[(i,j)]
        
        return dfs(0,0)
        