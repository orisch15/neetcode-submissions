class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #the dictionery for the dups in the window
        dupset = set()
        l, max_len = 0, 0
        for r in range(len(s)):
            ch = s[r]
            while ch in dupset:
                left_ch = s[l]
                dupset.remove(left_ch)
                l+=1
            dupset.add(ch) 
            max_len = max(max_len, (r-l+1))
        return max_len


        