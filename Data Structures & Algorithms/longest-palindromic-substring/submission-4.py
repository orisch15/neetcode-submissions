class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        res = [-1,-1]
        l_res = 0
        i = 0
        while i < len(s):
            if i % 1 == 0:
                l, r = int(i) - 1, int(i) + 1
            else:
                l, r = int(i), int(i) + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= l_res:
                    res = [l, r]
                    l_res = r - l + 1
                l -= 1
                r += 1

            i += 0.5

        return s[res[0]: res[1]+1]