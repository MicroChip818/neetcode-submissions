class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counts = []
        for num in nums:
            if num not in num_counts:
                num_counts.append(num)
                continue
            return True
        return False
        