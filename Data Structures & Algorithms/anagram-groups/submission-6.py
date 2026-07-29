class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            pattern = 26 * [0]
            
            for i, c in enumerate(s):
                pattern[ord(c) - ord('a')] += 1
            pattern = tuple(pattern)

            if pattern in anagrams:
                anagrams[pattern].append(s)
            else:
                anagrams[pattern] = [s]

        return [*anagrams.values()]