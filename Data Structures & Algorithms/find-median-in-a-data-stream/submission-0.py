class MedianFinder:
    #min heap for the big ones and max for the small ones
    #if num > mid so put it in the min heap and vv
    #if size diff is >=2 pop the min/max and add to the other

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            #max heap needs to multiply by -1 to act as max
            heapq.heappush(self.small, -1 * num)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        elif len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)

    def findMedian(self) -> float:
        #not equal so odd
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        #even
        return (-1 * self.small[0] + self.large[0]) / 2.0

        
        