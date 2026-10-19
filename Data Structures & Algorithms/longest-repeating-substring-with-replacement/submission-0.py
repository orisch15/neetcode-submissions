class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #a dict for counting the frequencies of the charecters in the substring
        #the max size of counts will be 26!!! so finding max will be O(1)
        counts = {}
        l, max_len, maxf = 0, 0, 0

        for r in range(len(s)):
            char = s[r]
            if char not in counts:
                counts[char] = 1
            else: 
                counts[char] += 1
            
            #takes O(1)
            maxf = max(set(counts.values()))

            while (r - l + 1) - maxf > k:
                counts[s[l]] -= 1
                maxf = max(set(counts.values()))
                l+=1

            max_len = max(max_len, r - l + 1)

        return max_len

        