class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for ops in operations:
            if ops == "+":
                scores.append(scores[-1] + scores[-2])
            elif ops == "D":
                scores.append(scores[-1] * 2)
            elif ops == "C":
                scores.pop()
            else:
                scores.append(int(ops))
        print(scores)
        return sum(scores)