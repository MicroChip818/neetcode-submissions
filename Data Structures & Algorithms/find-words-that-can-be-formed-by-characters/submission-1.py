from copy import copy

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        list_chars = list(chars)

        for word in words:
            if all([word.count(char) <= chars.count(char) for char in word]):
                res += len(word)

        return res