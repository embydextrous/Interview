from heapq import heappush, heappop, heapreplace
from random import randint

class Median:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.median = None

    def process(self, x):
        if self.median is None:
            heappush(self.minHeap, x)
            self.median = x
        elif len(self.maxHeap) == len(self.minHeap):
            if x > -self.maxHeap[0]:
                heappush(self.minHeap, x)
                self.median = self.minHeap[0]
            else:
                heappush(self.maxHeap, -x)
                self.median = -self.maxHeap[0]
        else:
            if len(self.minHeap) > len(self.maxHeap):
                if x > self.minHeap[0]:
                    heappush(self.maxHeap, -self.minHeap[0])
                    heapreplace(self.minHeap, x)
                else:
                    heappush(self.maxHeap, -x)
            else:
                if x < -self.maxHeap[0]:
                    heappush(self.minHeap, -self.maxHeap[0])
                    heapreplace(self.maxHeap, -x)
                else:
                    heappush(self.minHeap, x)
            self.median = (self.minHeap[0] - self.maxHeap[0]) / 2.0


median = Median()
a = [randint(1, 50) for i in range(20)]
print(a)
for i in a:
    median.process(i)
    print(median.median)