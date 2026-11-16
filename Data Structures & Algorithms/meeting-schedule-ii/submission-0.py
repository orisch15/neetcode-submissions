"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sort by starting point to make sure
        intervals.sort(key = lambda x:x.start)
        #min heap is required to make the rooms packed togheter
        heap = []

        for inter in intervals:
            start, end = inter.start, inter.end
            if heap and heap[0] <= start:
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)
        
        return len(heap)

        
        