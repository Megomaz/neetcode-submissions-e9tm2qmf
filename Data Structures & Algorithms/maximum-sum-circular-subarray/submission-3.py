class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # intuition: “Take the total array sum and REMOVE a bad middle part”

        cur_min = cur_max = total = 0
        global_max = -float('inf')
        global_min = float('inf')

        for num in nums:
            cur_max += num
            cur_max = max(cur_max, num)
            global_max = max(global_max, cur_max)

            total += num

            cur_min += num
            cur_min = min(cur_min, num)
            global_min = min(global_min, cur_min)
        # Intu
        return max(total - global_min,global_max)  if total - global_min > 0 else global_max


                





