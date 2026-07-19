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
            if c in t_freq:
                t_freq[c] += 1
            else:
                t_freq[c] = 1
            
        for c, f in s_freq.items():
            if c in t_freq and f == t_freq[c]:
                continue
            return False

        for c, f in t_freq.items():
            if c in s_freq and f == s_freq[c]:
                continue
            return False

        return True
