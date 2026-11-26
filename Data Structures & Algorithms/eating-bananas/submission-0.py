class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        M = -1
        # O(n) - find the maximum pile, it will be the largest k possible
        for count in piles:
            M = max(M, count)
        
        small, big = 1, M
        ans = big
        
        while small <= big:
            k = (small + big) // 2
            res = self.check(k, h, piles)
            # overspeed or equal, bcause res == 0 doesnt mean finish
            if res >= 0:
                ans = k
                big = k - 1           

            elif res < 0:
                small = k + 1
        return ans

    def check(self, speed, tempH, piles):
        for count in piles:
            timeToEat = math.ceil(count / speed)
            tempH -= timeToEat

        return tempH