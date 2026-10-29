class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i, r, c):

            if i == len(word):
                return True
            if (c < 0 or c >= COLS or r < 0 or r >= ROWS or (r, c) in visited or board[r][c] != word[i]):
                return False

            visited.add((r,c))
            res = dfs(i+1, r+1, c) or dfs(i+1, r-1, c) or dfs(i+1, r, c+1) or dfs(i+1, r, c-1)
            visited.remove((r,c))

            return res

        #starting from each cell as the index = 0
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        return False