class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        total = sum(piles)
        half = total // 2

        def dfs(l,r, A):
            if l >= r:
                return 0

            if (l,r) in dp:
                return dp[(l,r)]

            if A:
                alice_score = max(piles[l] + dfs(l + 1,r,not A), piles[r] + dfs(l, r - 1, not A))
            else:
                alice_score = min(dfs(l + 1,r, not A), dfs(l + 1,r, not A))

            dp[(l,r)] = alice_score
            return alice_score
        
        return half - dfs(0,len(piles) - 1,True) < 0