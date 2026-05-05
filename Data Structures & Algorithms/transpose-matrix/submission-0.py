class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # rows = cols
        # cols = rows
        rows,cols = len(matrix), len(matrix[0])
        grid = [[0] * rows for _ in range(cols) ]

        for row in range(rows):
            for col in range(cols):
                grid[col][row] = matrix[row][col]

        return grid

        