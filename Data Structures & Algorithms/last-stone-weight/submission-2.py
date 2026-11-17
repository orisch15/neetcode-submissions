class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap) #O(n)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            
            if x > y:
                smash = x - y
                heapq.heappush(heap, -smash)
            elif y > x:
                smash = y - x
                heapq.heappush(heap, -smash)
        
        if len(heap) == 1:
            return -heap[0]

        return 0

        