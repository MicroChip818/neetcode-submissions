class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        correct_range = set([i for i in range(1, len(nums) + 1)])

        for num in nums:
            if num in correct_range:
                correct_range.discard(num)

        return list(correct_range)