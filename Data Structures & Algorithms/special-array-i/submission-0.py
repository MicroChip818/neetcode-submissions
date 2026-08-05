class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = "even" if nums[0] % 2 != 0 else "odd"
        
        for num in nums:
            if (parity == "even" and num % 2 == 0) or (parity == "odd" and num % 2 != 0):
                return False
            parity = "odd" if parity == "even" else "even"

        return True