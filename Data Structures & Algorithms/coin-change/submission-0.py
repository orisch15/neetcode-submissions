class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(i, total):
            # תנאי העצירה המעודכנים
            if total == amount:
                return 0
            if total > amount or i >= len(coins):
                return -1
            
            if (i, total) in memo:
                return memo[(i, total)]
            
            # שלבי הרקורסיה
            take = dfs(i, total + coins[i])
            move = dfs(i + 1, total)
            
            # ניהול הסוכם: מוסיפים 1 רק אם לקחנו מטבע והמסלול חוקי
            if take != -1:
                take += 1
            
            # סינון מסלולים לא חוקיים באמצעות הטריק שלך
            if take != -1 and move != -1:
                ans = min(take, move)
            else:
                ans = max(take, move)
                
            # שמירת התוצאה והחזרתה
            memo[(i, total)] = ans
            return ans

        return dfs(0, 0)