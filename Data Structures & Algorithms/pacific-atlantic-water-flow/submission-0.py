class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #check the opposit cond, if the water can climb to the high
        diractions = [[1,0], [0,1], [-1,0], [0,-1]]
        ROWS, COLS = len(heights), len(heights[0])
        pas, atl = set(), set()

        def dfs(r,c, visit):

            visit.add((r,c))
            for dr, dc in diractions:
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in visit and nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, visit)


        #row = 0\-1 trans
        for c in range(COLS):
            dfs(0, c, pas)
            dfs(ROWS - 1, c, atl)
        
        for r in range(ROWS):
            dfs(r, 0,  pas)
            dfs(r, COLS - 1, atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pas and (r, c) in atl:
                    res.append([r, c])

        return res