class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        rows, cols = len(matrix), len(matrix[0])
        row_zero = [False] * rows
        col_zero = [False] * cols
    
    # First pass: mark rows/cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zero[i] = True
                    col_zero[j] = True
    
    # Second pass: apply zeros
        for i in range(rows):
            for j in range(cols):
                if row_zero[i] or col_zero[j]:
                    matrix[i][j] = 0
        