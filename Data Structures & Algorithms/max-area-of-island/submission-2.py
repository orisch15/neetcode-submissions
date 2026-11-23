class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        visit = set()
        def dfs(r,c):
            visit.add((r,c))

            count = 0
            for dr in directions:
                nr, nc = r + dr[0], c + dr[1]
                
                if (nr, nc) not in visit and (nr < ROWS and nr >= 0 and nc < COLS and nc >= 0):
                    if grid[nr][nc] == 1:
                        count += dfs(nr, nc)

            return 1 + count


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == 1:
                    island = dfs(r,c)
                    res = max(res, island)
        return res


        