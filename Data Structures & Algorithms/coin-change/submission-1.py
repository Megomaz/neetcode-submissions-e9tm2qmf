class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def backtrack(amount):
            if amount == 0:
                return 0
            
            if amount < 0:
                return float('inf')
            
            if amount in dp:
                return dp[amount]

            res = float('inf')

            for c in coins:
                res = min(res, 1 + backtrack(amount - c))
            
            dp[amount] = res
            return res
        ans = backtrack(amount)
        return -1 if ans == float('inf') else ans