class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        dp = {}
        half = total // 2
        def dfs(i, remaining):
            if i == len(stones):
                return abs(remaining)
            
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            

            res = min(dfs(i+1,remaining - stones[i]),dfs(i+1,remaining) )
            dp[(i, remaining)] = res
            return res

        val = dfs(0, half) # smallest diff around half of total
        best_subset = half - val

        return total - 2 * best_subset