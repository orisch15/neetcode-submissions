class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for s in strs:
            word += str(len(s)) + "#" + s
        return word

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1

            length = int(s[i:j])
            arr.append(s[j+1:j+length+1])
            i = j+1+length
            j = i


        return arr





