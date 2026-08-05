class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        res = 0

        for i, height in enumerate(heights):
            if height != sorted_heights[i]:
                res += 1
        
        return res