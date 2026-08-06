class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_map = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        
        for c in text:
            if c in balloon_map:
                balloon_map[c] += 1

        balloon_map["l"] /= 2
        balloon_map["o"] /= 2

        return int(min([*balloon_map.values()]) // 1)