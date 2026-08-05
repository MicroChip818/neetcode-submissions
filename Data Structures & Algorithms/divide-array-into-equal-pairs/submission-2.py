class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq_map = {}
        
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        for freq in freq_map.values():
            if freq % 2 != 0:
                return False
            
        return True