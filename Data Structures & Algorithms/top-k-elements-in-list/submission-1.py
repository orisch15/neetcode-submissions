import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        maxHeap = []
        for n in nums:
            if n not in counts: counts[n] = 1
            else: counts[n]+=1

        for i in counts:
            heapq.heappush(maxHeap, (-counts[i],i))

        res = []
        for _ in range(k):
            neg_freq, num = heapq.heappop(maxHeap)
            res.append(num)
        return res

        
        