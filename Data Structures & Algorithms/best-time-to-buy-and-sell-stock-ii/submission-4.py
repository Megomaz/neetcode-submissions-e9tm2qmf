class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, bought):
            if i >= len(prices):
                return 0
            
            if (i, bought) in dp:
                return dp[(i,bought)]
            
            res = 0

            if bought:
                # sell a stock
                res = max(res,prices[i] + dfs(i+1,not bought), dfs(i+1,bought))
            else:    
                # buy a stock
                res = max(res, -prices[i] + dfs(i+1,not bought),dfs(i+1,bought))
            
            
            dp[(i, bought)] = res
            return res
        return dfs(0,False)
            


        