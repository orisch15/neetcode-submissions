class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0:
            return False
        dic = {
            "]" :"[",
            "}" :"{",
            ")" :"(" }
        st = []

        for b in s:
            if b not in dic:
                st.append(b)
            else:
                if len(st) == 0:
                    return False
                if st.pop() != dic[b]:
                    return False
        return len(st) == 0
                    

            