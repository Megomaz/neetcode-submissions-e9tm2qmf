class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # M = 1
        # 1 ≤ X ≤ 2M -> player can take
        # e.g Alice takes 1, I take 1 ≤ x ≤ 2, Alice takes 1 ≤ x ≤ 4
        # also have to adjust M to be max of max(M,X)

        n = len(piles)
        M = 1
        cache = {}

        def game(is_Alice,M,idx):
            if idx >= n:
                return 0

            if (is_Alice,M,idx) in cache: 
                return cache[(is_Alice,M,idx)]
            
            res = 0 if is_Alice else float('inf')
            total_stones = 0 

            for X in range(1, 2 * M + 1):
                if idx + X > n:
                    break

                total_stones += piles[idx + X - 1]
                
                if is_Alice:
                    res = max(res, total_stones + game(False,max(M,X),X + idx))
                else:
                    res = min(res, game(True,max(M,X),X + idx,))

            cache[(is_Alice,M,idx)] = res
            return res

        return game(True,1,0)

