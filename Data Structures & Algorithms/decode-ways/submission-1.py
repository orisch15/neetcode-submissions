from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i == len(s):
                return 1
            if i > len(s) or s[i] == "0":
                return 0

            if i < len(s) - 1 and int(s[i] + s[i+1]) <= 26:
                return dp(i + 1) + dp(i + 2)

            else:
                return dp(i + 1)
        
        return dp(0)

            
        