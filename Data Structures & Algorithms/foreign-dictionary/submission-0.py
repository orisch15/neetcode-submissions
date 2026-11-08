class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #מיון טופולוגי!
        #בניית הגרף תעשה באמצעות מעבר על הרשימה
        #לשים לב למקרה קצה שפוסל ישר אם מילה שהיא קדימונת של מילה שלפני מופיעה
        if not words:
            return ""
        #create adj list
        adj = {c : set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            #the prefix edge case
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        #create the pre requireties for dfs with color
        color = {s:"w" for s in adj}
        res = []

        def dfs(c):
            color[c] = "g"
            for nei in adj[c]:
                if color[nei] == "g":
                    return False
                if color[nei] == "w":
                    if not dfs(nei):
                        return False
            color[c] = "b"
            res.append(c)
            return True

        for char in adj:
            if color[char] == "w":
                if not dfs(char):
                    return ""

        res.reverse()
        return "".join(res)

