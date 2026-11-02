class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
           
            res = False
            j = i
            while j<len(s):
                word = s[i: j + 1]
                if word in wordDict:
                    if dfs(j+1):
                        res = True
                j += 1

            memo[i] = res

            return memo[i]
        
        return dfs(0)

        