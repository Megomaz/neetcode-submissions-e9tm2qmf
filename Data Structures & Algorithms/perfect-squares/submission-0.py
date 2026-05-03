import math
class Solution:
    def numSquares(self, n: int) -> int:
        squares = int(math.sqrt(n))
        
        arr_sqrs = [float('inf')] * (n + 1)
        arr_sqrs[0] = 0

        for i in range(1, n + 1):
            for j in range(1,squares+1):
                if i - (j*j) >= 0:
                    arr_sqrs[i] = min(arr_sqrs[i - (j*j)] + 1,arr_sqrs[i]) 

        
        return arr_sqrs[n] 
