class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        
        for word in words:
            if all([c in allowed for c in word]):
                res += 1

        return res 