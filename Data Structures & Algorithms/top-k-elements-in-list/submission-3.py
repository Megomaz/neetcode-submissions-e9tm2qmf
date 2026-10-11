class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        return [x[0] for x in sorted(count.items(),key=lambda x:x[1],reverse=True)[:k]]