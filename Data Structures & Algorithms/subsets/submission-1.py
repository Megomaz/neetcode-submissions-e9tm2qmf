class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i,arr):
            if i == len(nums):
                res.append(arr[:])
                return
            
            dfs(i+1, arr)

            arr.append(nums[i])
            dfs(i+1, arr)
            arr.pop()
        dfs(0,[])
        return res