class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4:
            return False
        
        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        square = [0] * 4

        def backtrack(i):
            if i == len(matchsticks):
                if all (side == target for side in square):
                    return True

                return False
            
            for k in range(4):
                if square[k] + matchsticks[i] > target:
                    continue
                
                square[k] += matchsticks[i]

                if backtrack(i+1):
                    return True

                square[k] -= matchsticks[i]
            return False

        return backtrack(0)


        
                