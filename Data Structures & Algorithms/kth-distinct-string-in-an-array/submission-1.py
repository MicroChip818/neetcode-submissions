class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq_map = {}
        for s in arr:
            if s in freq_map:
                freq_map[s] += 1
            else:
                freq_map[s] = 1
        
        count = 0
        for s, freq in freq_map.items():
            if freq == 1:
                count += 1

            if count == k:
                return s

        return ""