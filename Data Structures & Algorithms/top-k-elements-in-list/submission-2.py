class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for i in range(len(nums))]
        res = []
        for n in nums:
            if n not in counts: counts[n] = 1
            else: counts[n]+=1

        for c in counts: 
            buckets[counts[c]-1].append(c)
        
        i=len(buckets)-1
        while len(res) < k:
            for n in buckets[i]:
                res.append(n)
            i-=1
        
        return res



