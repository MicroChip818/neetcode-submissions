class Solution:
    def maxDifference(self, s: str) -> int:
        freq_map = {}

        for c in s:
            if c in freq_map:
                freq_map[c] += 1
            else:
                freq_map[c] = 1

        max_freq = 0
        min_freq = len(s)

        for freq in freq_map.values():
            if freq % 2 == 0:
                min_freq = min(min_freq, freq)
            else:
                max_freq = max(max_freq, freq)

        return max_freq - min_freq