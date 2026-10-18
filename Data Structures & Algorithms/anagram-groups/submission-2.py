class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for w in strs:
            ws = ''.join(sorted(w))
            if ws not in dic:
                dic[ws] = [w]
            else: 
                dic[ws].append(w)

        out = []
        for k in dic:
            out.append(dic[k])

        return out
        