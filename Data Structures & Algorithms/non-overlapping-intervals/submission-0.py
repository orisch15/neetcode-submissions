class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #מיון לפי זמני סיום
        intervals.sort(key = lambda x:x[1])
        lastEnd = float('-inf')
        removed = 0
        for start, end in intervals:
            if start >= lastEnd:
                lastEnd = end
            else:
                removed += 1
        
        return removed

        
        