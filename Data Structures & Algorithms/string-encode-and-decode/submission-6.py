class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "-1"
        
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if s == "-1":
            return []

        res = []
        state = "length"
        num_digits = []
        temp = []

        for c in s:
            if state == "length":
                if c == "#":
                    num_digits = int("".join(num_digits))
                    state = "string"
                    if num_digits == 0:
                        res.append("")
                        state = "length"
                        num_digits = []
                    continue
                num_digits.append(c)

            elif state == "string":
                temp.append(c)
                num_digits -= 1
                if num_digits == 0:
                    num_digits = []
                    state = "length"
                    res.append("".join(temp))
                    temp = []

        return res
