class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)
    #how to determin in which squere are we in? 
    # if we do integer division we can code the row number to 1-3

        for r in range(len(board[0])):
            for c in range(len(board[0])):

                if board[r][c] == ".": continue
                
                if (board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in sqrs[(r//3,c//3)]):
                   return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqrs[(r//3,c//3)].add(board[r][c])
        
        return True
        