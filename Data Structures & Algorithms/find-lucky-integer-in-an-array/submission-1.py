class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_map = {}
        for n in arr:
            if n in freq_map:
                freq_map[n] += 1
            else:
                freq_map[n] = 1

        res = -1
        for num, freq in freq_map.items():
            if num == freq and num > res:
                res = num

        return res