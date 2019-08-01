"""
295. Median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Design a data structure that supports the following two operations:
void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
"""
from heapq import *

class MedianFinder:

    def __init__(self):

        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        if len(self.minHeap) == len(self.maxHeap):
            heappush(self.maxHeap,-heappushpop(self.minHeap,-num))
        else:
            heappush(self.minHeap,-heappushpop(self.maxHeap,num))


    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return float(self.maxHeap[0]-self.minHeap[0])/2.0
        else:
            return self.maxHeap[0]

def main():
    mf = MedianFinder()
    mf.addNum(1)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())

if __name__ == "__main__":
    main()