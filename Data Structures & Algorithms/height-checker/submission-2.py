import heapq
from copy import copy

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copy_heights = copy(heights)
        heapq.heapify(copy_heights)
        sorted_heights = []
        
        while copy_heights:
            sorted_heights.append(heapq.heappop(copy_heights))

        res = 0
        for i, height in enumerate(heights):
            if height != sorted_heights[i]:
                res += 1
        
        return res