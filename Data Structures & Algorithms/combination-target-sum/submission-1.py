class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,arr,total):
            if total == target:
                res.append(arr[:])
                return

            if total > target or i == len(nums):
                return
            
            dfs(i+1,arr,total)

            arr.append(nums[i])
            dfs(i,arr,total + nums[i])
            arr.pop()
            total -= nums[i]
        dfs(0,[],0)
        return res
            

