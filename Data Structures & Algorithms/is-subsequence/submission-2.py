class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Iterate through t
        res = []
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                res.append(s[i])
                i += 1
        
        return "".join(res) == s