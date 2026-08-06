class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        res = []
        seen = set()

        for num in nums2:
            if num in set1 and num not in seen:
                res.append(num)
                seen.add(num)

        return res