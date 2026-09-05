class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        maps = {q:-1 for q in queries}
        res = []
        heap = [] # [interval length, right idx]

        intervals.sort()
        
        r = 0
        
        for q in sorted(queries):
                
            
            while r < len(intervals) and intervals[r][0] <= q:
                left, right = intervals[r]
                length = right - left + 1

                heapq.heappush(heap,(length, right))
                r += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap and maps[q] == -1:
                maps[q] = heap[0][0]
        
        
        return [maps[q] for q in queries]

        