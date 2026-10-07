class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        memo = {}
        # min of max
        def dfs(i,m):
            if m == 1:
                return sum(nums[i:])
            
            if (i,m) in memo:
                return memo[(i,m)]
            
            sub_arr_sum = 0
            best = float('inf')
            for j in range(i,len(nums) - m + 1):
                sub_arr_sum += nums[j]

                res = max(sub_arr_sum,dfs(j+1, m - 1))
                best = min(best,res)
            
            memo[(i,m)] = best
            return best

        return dfs(0,k)
