class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        freq_map = {num: freq for num, freq in sorted(freq_map.items(), key = lambda item: item[1], reverse=reversed)}
        res = []

        for num, freq in freq_map.items():
            res.append(num)
            if len(res) == k:
                return res