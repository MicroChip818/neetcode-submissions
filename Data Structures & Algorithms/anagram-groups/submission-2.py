class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        anagram_groups = []

        for s in strs:
            anagrams.append([s, [0] * 26])
            for i, _ in enumerate(s):
                anagrams[-1][1][ord(s[i]) - ord('a')] += 1
            anagrams[-1][1] = tuple(anagrams[-1][1])

        curr_index = -1
        seen_anagrams = {}

        for anagram in anagrams:
            if anagram[1] in seen_anagrams:
                group_index = seen_anagrams[anagram[1]]
                anagram_groups[group_index].append(anagram[0])
            else:
                anagram_groups.append([anagram[0]])
                seen_anagrams[anagram[1]] = len(anagram_groups) - 1
        
        print(anagram_groups)
        return anagram_groups
