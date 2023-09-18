class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        row = len(grid)
        col = len(grid[0])
        # def checkGrid(i,j):
        #     if (i not in range(row)) or (j not in range(col)):
        #         return False
        #     if grid[i][j] == '1':
        #         return True
        #     return False
        def fillGrid(i, j):
            if (i not in range(row)) or (j not in range(col)):
                return
            if grid[i][j] == '1':
                grid[i][j] = '2'
                if i >= 1 and grid[i-1][j] == '1':
                    fillGrid(i-1, j)
                if i < row-1 and grid[i+1][j] == '1':
                    fillGrid(i+1, j)
                if j >= 1 and grid[i][j-1] == '1':
                    fillGrid(i, j-1)
                if j < col-1 and grid[i][j+1] == '1':
                    fillGrid(i, j+1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    counter += 1
                    fillGrid(i,j)
        # print(grid)
        return counter

        