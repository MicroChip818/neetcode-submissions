class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "\u03A9 NONE"
        return "\u03A9".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "\u03A9 NONE":
            return []
        return s.split("\u03A9")