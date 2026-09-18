class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 1 = 3
        # 0 = 4
        # 2 = 2
        # 3 = 1
        self.perimeter = 0
        rows,cols = len(grid), len(grid[0])
        directions = [[0,1],[-1,0],[1,0], [0,-1]]
        seen = set()

        def dfs(row,col):
            if ((row,col) in seen) or not (0 <= row < rows and 0 <= col < cols) or grid[row][col] == 0:
                return

            count = 4
            seen.add((row,col))

            for dr,dc in directions:
                nr, nc = row + dr, dc + col
                if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == 0:
                    continue

                count -= 1
            
            self.perimeter += count
            dfs(row + 1,col)
            dfs(row - 1, col)
            dfs(row,col + 1)
            dfs(row, col - 1)

            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r,c)
                    break
        
        return self.perimeter