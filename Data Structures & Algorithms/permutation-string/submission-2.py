from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = Counter(s1)
        window = {}
        l = 0
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1
        if window == count1:
            return True
        for r in range(len(s1), len(s2)): 
            ch_left, ch_right = s2[l], s2[r]
            window[ch_right] = window.get(ch_right, 0) + 1
            window[ch_left] -= 1
            if window[ch_left] == 0:
                del window[ch_left]
            l += 1
            if window == count1:
                return True


        return False



        
        