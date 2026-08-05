class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        n = len(t)
        res = n
        i = 0
    
        for c in s:
            if i < len(t) and t[i] == c:
                res -= 1
                i += 1

        return res