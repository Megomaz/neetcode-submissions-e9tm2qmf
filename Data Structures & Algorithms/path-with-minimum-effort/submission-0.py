class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []
        rows,cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        heapq.heappush(heap,(0,0,0))
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = 0
        while heap:
            diff,row,col = heapq.heappop(heap)
            
            if diff > dp[row][col]:
                continue
            if row == rows - 1 and col == cols - 1:
                return diff
            for dr, dc in directions:
                nr,nc = dr + row, dc + col

                if (0 <= nr < rows) and (0 <= nc < cols):
                    new_diff = max(diff,abs(heights[row][col] - heights[nr][nc]))
                    if diff < dp[nr][nc]:
                        dp[nr][nc] = new_diff
                        heapq.heappush(heap,(new_diff,nr,nc))
        print(dp)            
    
        return 0