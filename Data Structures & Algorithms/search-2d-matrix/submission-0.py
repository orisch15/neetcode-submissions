class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS - 1
        targetRow = -1
        # binary search to find the correct row
        while l <= r:
            mid = (l + r) // 2
            start, end = matrix[mid][0], matrix[mid][-1]

            if target > end:
                l = mid + 1
            elif target < start:
                r = mid - 1
            else:
                targetRow = mid
                break
        if targetRow == -1:
            return False

        l, r = 0, COLS - 1
        targetCol = -1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[targetRow][mid]:
                l = mid + 1
            elif target < matrix[targetRow][mid]:
                r = mid - 1
            else:
                targetCol = mid
                break
        
        return targetCol != -1

                
        