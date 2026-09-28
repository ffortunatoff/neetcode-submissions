class Solution:
    def calPoints(self, operations: List[str]) -> int:
        proper_score = []

        for op in operations:
            if op == '+':
                proper_score.append(proper_score[-1] + proper_score[-2])
            elif op == 'D':
                proper_score.append(proper_score[-1] * 2)
            elif op == 'C':
                proper_score.pop()
            else:
                proper_score.append(int(op))

        return sum(proper_score)
