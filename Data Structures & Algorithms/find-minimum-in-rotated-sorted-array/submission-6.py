class Solution:
    def findMin(self, nums: List[int]) -> int:
        cur_min = nums[0]

        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            left = nums[m -1] if 0 <= m - 1 else -1001
            right = nums[m + 1] if m+1 < len(nums) else 1001

            if nums[m] > right:
                return right
            elif cur_min < nums[m]:
                l = m + 1
            else:
                cur_min = nums[m]
                r = m - 1

        return cur_min