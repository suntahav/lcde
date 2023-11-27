class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # O(m+n)
        rows = [1] * ROWS
        cols = [1] * COLS

        #handle rows 
        for i in range(ROWS):
            for j in range(COLS):
                rows[i] *= matrix[i][j]
                cols[j] *= matrix[i][j]
        
        #Inplace operation
        for i in range(ROWS):
            for j in range(COLS):
                if rows[i] == 0 or cols[j] == 0:
                    matrix[i][j] = 0
