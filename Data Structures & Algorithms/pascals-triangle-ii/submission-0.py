class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #we will work bottom up
        oldRow = [1]
        newRow = [1]

        for i in range(1, rowIndex + 1):
            newRow = [1] * (i + 1)
            for j in range(1, i):

                newRow[j] = oldRow[j - 1] + oldRow[j]

            oldRow = newRow
        
        return newRow


        