"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)<=1:
            return True
        sorted_int = sorted(intervals, key = lambda x:x.start)
        
        for i in range(len(sorted_int) - 1):
            if sorted_int[i].end > sorted_int[i+1].start:
                return False
        
        return True