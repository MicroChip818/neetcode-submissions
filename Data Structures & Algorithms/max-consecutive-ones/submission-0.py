class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        temp = 0

        for num in nums:
            if num == 1:
                temp += 1
            else:
                res = max(temp, res)
                temp = 0

        return max(res, temp)