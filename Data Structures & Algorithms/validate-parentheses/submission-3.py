class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        parentheses = []
        if len(s) == 1 or s[0] in pairs.values():
            return False

        for c in s:
            parentheses.append(c)
            if parentheses[-1] in pairs.values():
                if len(parentheses) == 1 or parentheses[-1] != pairs[parentheses[-2]]:
                    return False
                else:
                    parentheses.pop()
                    parentheses.pop()

        return not parentheses