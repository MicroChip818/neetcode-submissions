class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return " -> "

        for i, s in enumerate(strs):
            if s == "":
                strs[i] = "'!empty!'"

        print(" -> ".join(strs))
        return " -> ".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == " -> ":
            return []

        list_strs = s.split(" -> ")
        for i, st in enumerate(list_strs):
            if st == "'!empty!'":
                list_strs[i] = ""

        return list_strs