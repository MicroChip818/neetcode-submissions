class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monotone = None

        for i, num in enumerate(nums):
            # Determine monotone
            if i == 0:
                continue
            if not monotone:
                monotone = "increasing" if nums[i] > nums[i - 1] else "decreasing" if nums[i] < nums[i - 1] else None
            elif (monotone == "increasing" and nums[i] < nums[i - 1]) or (monotone == "decreasing" and nums[i] > nums[i - 1]):
                return False

        return True