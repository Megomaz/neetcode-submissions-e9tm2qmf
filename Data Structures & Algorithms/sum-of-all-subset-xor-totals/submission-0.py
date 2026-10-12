class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0

        def dfs(i,arr):
            if i == len(nums):
                res = 0
                for n in arr:
                    res ^= n
                self.total += res
                return
            
            arr.append(nums[i])
            dfs(i+1, arr)
            arr.pop()

            dfs(i+1, arr)
        dfs(0,[])
        return self.total