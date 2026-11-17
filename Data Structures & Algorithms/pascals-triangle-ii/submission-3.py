class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        
        for r in range(1, rowIndex + 1):
            # מוסיפים את ה-1 החדש של סוף השורה
            row.append(1)
            
            # מעדכנים מימין לשמאל (מהאיבר שלפני האחרון עד אינדקס 1)
            for c in range(r - 1, 0, -1):
                row[c] += row[c - 1]
                
        return row