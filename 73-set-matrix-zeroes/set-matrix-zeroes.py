class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        flag_row = False
        flag_col = False
        for i in range(COLS):
            if matrix[0][i] == 0:
                flag_row = True
        for i in range(ROWS):
            if matrix[i][0] == 0:
                flag_col = True

        #handle rows 
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        #Inplace operation
        
        for i in range(1, ROWS):
            for j in range(1,COLS):
                if matrix[i][0] == 0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        
        if flag_row:
            for i in range(COLS):
                matrix[0][i] = 0
        if flag_col:
            for i in range(ROWS):
                matrix[i][0] = 0