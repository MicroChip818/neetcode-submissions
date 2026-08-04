import heapq
from copy import copy

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.arr, num)

    def findMedian(self) -> float:
        arr = copy(self.arr)
        length = len(self.arr)
        lower_half = []
        while len(lower_half) < (length // 2 + 1):
            lower_half.append(heapq.heappop(arr))

        if length % 2 != 0:
            return lower_half[-1]
        else:
            return (lower_half[-2] + lower_half[-1]) / 2

        
        