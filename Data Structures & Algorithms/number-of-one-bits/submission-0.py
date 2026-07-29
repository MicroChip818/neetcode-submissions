class Solution:
    def hammingWeight(self, n: int) -> int:
        formatted = str(bin(n)).lstrip('0b')
        return sum([int(c) for c in formatted])