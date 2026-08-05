class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq_map = {}
        
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        res = 0
        for freq in freq_map.values():
            if freq == 1:
                continue
            res += sum([n for n in range(1, freq)])

        return res