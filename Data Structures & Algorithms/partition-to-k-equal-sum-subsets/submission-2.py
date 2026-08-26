class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False for _ in range(len(nums))]

        def backtrack(i, subSetSum, K):
            if K == 0:
                return True

            if subSetSum == 0:
                return backtrack(0,target,K - 1)

            for x in range(i,len(nums)):
                if used[x] or subSetSum - nums[x] < 0:
                    continue

                used[x] = True
                if backtrack(x+1,subSetSum - nums[x], K):
                    return True

                used[x] = False
                
            return False
                    
        
        return backtrack(0,target,k)