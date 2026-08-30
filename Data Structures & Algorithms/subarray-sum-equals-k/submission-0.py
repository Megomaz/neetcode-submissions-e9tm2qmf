class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        prefix_seen = {0:1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_seen:
                res += prefix_seen[prefix_sum - k]
            
            prefix_seen[prefix_sum] = prefix_seen.get(prefix_sum, 0) + 1

        return res

        
