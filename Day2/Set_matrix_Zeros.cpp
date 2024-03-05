class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zero = set()
        col_zero = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        for row in row_zero:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

        for col in col_zero:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
