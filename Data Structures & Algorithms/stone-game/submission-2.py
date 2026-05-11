class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        # cleaner code
        def dfs(l, r):
            if l == r:
                return piles[l]

            if (l, r) in cache:
                return cache[(l, r)]

            left = piles[l] - dfs(l + 1, r)
            right = piles[r] - dfs(l, r - 1)

            cache[(l, r)] = max(left, right)
            return cache[(l, r)]

        return dfs(0, len(piles) - 1) > 0