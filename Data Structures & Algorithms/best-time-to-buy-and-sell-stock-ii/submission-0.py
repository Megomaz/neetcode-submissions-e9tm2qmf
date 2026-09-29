class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        
        # 7 6 8

        for idx, p in enumerate(prices):
            if idx == 0:
                continue
            if p > prices[idx -1]:
                total += p - prices[idx -1]
        return total
            


        