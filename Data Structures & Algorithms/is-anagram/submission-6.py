class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = 26 * [0]
        for i, _ in enumerate(s):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for f in freq:
            if f != 0:
                return False
        
        return True