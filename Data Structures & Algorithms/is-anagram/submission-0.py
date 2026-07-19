class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        s = list(s)
        t = list(t)
        for c in s:
            if c in t:
                t.remove(c)
            else:
                return False

        for c in t:
            if c in s:
                s.remove(c)
            else:
                return False

        return True