class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #BFS to iterate each node connected nodes
        #we will not visit 0 marked nodes, and after visiting node we will turn him 0
        ROWS, COLS = len(grid), len(grid[0])
        diractions = [[1,0], [0,1], [-1,0], [0,-1]]
        noIslands = 0

        def bfs(r, c):
            q = collections.deque()
            grid[r][c] = "0" # like coloring gray
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in diractions:
                    nr, nc = row + dr, col + dc
                    if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    noIslands += 1
        
        return noIslands


        