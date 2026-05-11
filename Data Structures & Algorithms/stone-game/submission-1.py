class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        n = len(piles)
        total = sum(piles)

        def dfs(A_turn,idx,l,r,score):
            if l == r:
                return score > total - score
                
            if (A_turn, idx) in cache:
                return cache[(A_turn, idx)]

            
            A_turn = True if not A_turn else False
            idx += 1
            left = dfs(A_turn,idx,l + 1,r,score + piles[l])
            right = dfs(A_turn,idx,l ,r - 1,score + piles[r])

            p = True if (left or right) else False
            cache[(A_turn, idx)] = p
            return p

        return dfs(True,0,0,n-1,0)
            
