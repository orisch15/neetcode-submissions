class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": 
            return ""
        t_dict = collections.Counter(t)
        win_dict = collections.defaultdict(int)
        l, min_sub, min_len = 0, [-1,-1], float("inf")

        for r in range(len(s)):
            win_dict[s[r]] += 1

            while self.is_valid(win_dict, t_dict):
                if min_len > r - l + 1:
                    min_sub = [l, r]
                    min_len = r - l + 1
                
                win_dict[s[l]] -= 1
                l += 1

        return s[min_sub[0] : min_sub[1] + 1] if min_len != float("inf") else ""

    #runs in O(128)
    def is_valid(self, win_dict, t_dict):
        for k in t_dict:
            if win_dict[k]<t_dict[k]:
                return False
        return True

        