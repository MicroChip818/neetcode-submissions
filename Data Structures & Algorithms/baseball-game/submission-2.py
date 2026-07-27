class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i, op in enumerate(operations):
            if op[-1].isdigit():
                score.append(int(op))
            elif op == '+':
                score.append(score[-1] + score[-2])
            elif op == 'C':
                score.pop()
            elif op == 'D':
                score.append(2 * score[-1])
        return sum(score)
        