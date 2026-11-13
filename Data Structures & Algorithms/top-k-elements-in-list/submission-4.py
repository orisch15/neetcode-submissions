from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #with bucket sort
        cnt = Counter(nums)
        buckets = [[] for i in range(len(nums))]
        res = []

        for c in cnt: 
            buckets[cnt[c]-1].append(c)

        i = len(buckets) - 1
        while len(res) < k:
            for n in buckets[i]:
                res.append(n)
            i -= 1
        return res

        