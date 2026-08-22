class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        max_freq = max([*freq_map.values()])
        grouped_freqs = [[] for i in range(max_freq)]
        res = []

        for num, freq in freq_map.items():
            grouped_freqs[freq - 1].append(num)

        for i in range(max_freq - 1, -1, -1):
            curr_freq = grouped_freqs[i]
            if curr_freq:
                for num in curr_freq:
                    res.append(num)
                    if len(res) == k:
                        return res
            