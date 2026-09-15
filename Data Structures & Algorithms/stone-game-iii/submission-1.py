class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # alice always starts 1st
        # take 1,2,3

        dp = {}

        def backtrack(i):
            if i >= len(stoneValue):
                return 0
            
            if (i) in dp:
                return dp[(i)]
            
            res,total = -float('inf'), 0

            for j in range(i, min(i + 3, len(stoneValue))):
                total += stoneValue[j]
                res = max(res, total - backtrack(j + 1))
            
            dp[(i)] = res
            return res
        
        ans = backtrack(0)

        if ans > 0:
            return 'Alice'
        elif ans == 0:
            return 'Tie'
        else:
            return 'Bob'