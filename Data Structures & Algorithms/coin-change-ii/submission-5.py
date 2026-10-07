class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        coins.sort()

        def dfs(i, total):
            if total == amount:
                return 1

            if i == len(coins):
                return 0

            if (i,total) in dp:
                return dp[(i,total)]

            res = 0
            if total + coins[i] <= amount:
                res += dfs(i+1, total) + dfs(i, total + coins[i])
            
            dp[(i,total)] = res
            return res
        return dfs(0,0)