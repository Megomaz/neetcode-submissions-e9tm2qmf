class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                idx,_ = stack.pop()
                res[idx] = i - idx
            stack.append((i,val))
        return res