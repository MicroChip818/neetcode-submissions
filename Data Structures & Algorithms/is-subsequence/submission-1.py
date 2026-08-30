class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True

        curr_s = -1

        for c in t:
            if c == s[curr_s + 1]:
                curr_s += 1
            if curr_s == len(s) - 1:
                return True
        
        return False