class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = {}
        l = 0

        for r in range(len(nums)):
            window[nums[r]] = window.get(nums[r],0) + 1

            if window[nums[r]] > 1:
                return True

            if r - l + 1 > k:
                window[nums[l]] -= 1
                l +=1
        
        return False