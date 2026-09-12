class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        nums.sort()
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for j in range(len(nums)):
                if used[j]:
                    continue     

                if j > 0 and nums[j] == nums[j-1] and used[j -1]:
                    continue
                
                used[j] = True
                curr.append(nums[j])

                backtrack(curr)

                curr.pop()
                used[j] = False

        backtrack([])
        return res

