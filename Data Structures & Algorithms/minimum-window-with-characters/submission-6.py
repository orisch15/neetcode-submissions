#have and need
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        t_dict = collections.Counter(t)
        win_dict = collections.defaultdict(int)
        l, min_sub, min_len = 0, [-1,-1], float("inf")
        need, have = len(t_dict), 0

        for r in range(len(s)):
            win_dict[s[r]] += 1

            if s[r] in t_dict and win_dict[s[r]] == t_dict[s[r]]:
                have += 1

            while need == have:
                if min_len > r - l + 1:
                    min_sub = [l, r]
                    min_len = r - l + 1
                win_dict[s[l]] -= 1
                if s[l] in t_dict and win_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1

        return s[min_sub[0] : min_sub[1] + 1] if min_len != float("inf") else ""

