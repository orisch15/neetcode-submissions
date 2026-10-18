class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for w in strs:
            ws = self.createUniqe(w)
            if ws not in dic:
                dic[ws] = [w]
            else: 
                dic[ws].append(w)

        out = []
        for k in dic:
            out.append(dic[k])

        return out

    def createUniqe(self, str):
        arr = [0]*26
        for s in str:
            arr[ord(s) - ord('a')]+=1
        return tuple(arr)
        