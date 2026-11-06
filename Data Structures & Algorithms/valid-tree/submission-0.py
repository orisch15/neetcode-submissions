class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #עץ הוא גרף קשיר ללא מעגלים
        #קשירות - נריץ די אף אס מצומת יחיד. אם לא כל הצמתים שחורים, זה לא עץ
        #נחפש תוך כדי קשת אחורית כדי לזהות מעגל
        color = ["w" for _ in range(n)]
        preMap = {i:[] for i in range(n)}
        self.res = True
        for node, nei in edges:
            preMap[node].append(nei)
            preMap[nei].append(node)

        def dfs(i, previos):
            color[i] = "g"

            for nei in preMap[i]:
                if color[nei] == "g" and nei != previos:
                    self.res = False

                if color[nei] == "w":
                    dfs(nei, i)
            color[i] = "b"
        
        dfs(0, -1)

        if "w" in color:
            self.res = False
        return self.res



        