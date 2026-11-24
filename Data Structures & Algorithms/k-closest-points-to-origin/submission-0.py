class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i, p in enumerate(points):
            x, y = p[0], p[1]
            dist.append([x**2 + y**2, x, y])
        heapq.heapify(dist)
        res = []
        while k > 0:
            p = heapq.heappop(dist)
            _, x, y = p
            res.append([x, y])
            k -= 1

        return res
        