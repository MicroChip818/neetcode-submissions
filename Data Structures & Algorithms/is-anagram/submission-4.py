class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}
        for c in s:
            if c in s_freq:
                s_freq[c] += 1
            else:
                s_freq[c] = 1
        
        for c in t:
            if c not in s_freq:
                return False
            if c in t_freq:
                t_freq[c] += 1
            else:
                t_freq[c] = 1
    
        for c in s_freq:
            if c not in t_freq or s_freq[c] != t_freq[c]:
                return False

        for c in t_freq:
            if c not in s_freq or s_freq[c] != t_freq[c]:
                return False

        return True