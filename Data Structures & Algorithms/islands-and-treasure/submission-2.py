class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        time = 0
        rows,cols = len(grid), len(grid[0])
        directions = [[0,1],[0,-1], [1,0], [-1,0]]
        visited = set()
        INF = 2147483647
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row,col))

        while q:
            size = len(q)
            for _ in range(size):
                row,col = q.popleft()

                if (row,col) in visited:
                    continue
                
                visited.add((row,col))
                grid[row][col] = time
                for dr, dc in directions:
                    nr,nc = dr + row, dc + col

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF and (nr,nc) not in visited:
                      q.append((nr,nc))  

            time += 1
        
