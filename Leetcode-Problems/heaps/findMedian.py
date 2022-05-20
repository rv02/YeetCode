import heapq

class MedianFinder:

    def __init__(self):
        self.minheap = [] #store the larger half
        self.maxheap = [] #store the smaller half

    def addNum(self, num: int) -> None:
        if self.minheap and num < self.minheap[0]:
            heapq.heappush(self.maxheap, -num)
            if len(self.maxheap) > len(self.minheap) + 1:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        else:
            heapq.heappush(self.minheap, num)
            if len(self.minheap) > len(self.maxheap) + 1:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))        

    def findMedian(self) -> float:
        if len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2



medianFinder = MedianFinder()
medianFinder.addNum(1);    # arr = [1]
medianFinder.addNum(2);    # arr = [1, 2]
medianFinder.findMedian(); # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    # arr[1, 2, 3]
medianFinder.findMedian(); # return 2.0
