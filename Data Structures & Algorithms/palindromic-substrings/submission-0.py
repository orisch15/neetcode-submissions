class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        i = 0
        while i < len(s):
            if i % 1 == 0:
                res += 1
                l, r = int(i) - 1, int(i) + 1
            else:
                l, r = int(i), int(i) + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            i += 0.5
        
        return res