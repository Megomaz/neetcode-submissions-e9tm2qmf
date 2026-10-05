class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        for r in range(self.rows):
            for c in range(1, self.cols):
                self.matrix[r][c] += self.matrix[r][c - 1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for r1 in range(row1,row2 + 1):
            valid = self.matrix[r1][col1 - 1] if col1 > 0 else 0
            total += self.matrix[r1][col2] - valid
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)