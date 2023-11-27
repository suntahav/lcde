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
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0
        
        #Inplace operation
        for i in range(ROWS):
            for j in range(COLS):
                if rows[i] == 0 or cols[j] == 0:
                    matrix[i][j] = 0
