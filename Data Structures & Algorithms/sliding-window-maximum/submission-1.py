import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max_heap = (val,idx)

        max_heap = []
        res = []

        for right in range(k):
            heapq.heappush(max_heap,(-nums[right],right))
        res.append(-max_heap[0][0])
        for r in range(right + 1,len(nums)):
            while max_heap and max_heap[0][1] < r - k + 1:
                heapq.heappop(max_heap)
            heapq.heappush(max_heap,(-nums[r],r))
            res.append(-max_heap[0][0])
            
            
            

        return res