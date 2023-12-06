class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def bfs(i, j):
            # print("Hello
            visited.add((i,j))
            q = collections.deque()
            q.append((i,j))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            length = 0
            
            while q:
                row, col = q.popleft()
                length += 1
                # print(length)
                for r,c in directions:
                    n_row = row + r
                    n_col = col + c
                    if (n_row in range(ROWS)) and (n_col in range(COLS)) and grid[n_row][n_col]==1 and ((n_row, n_col) not in visited):
                        visited.add((n_row, n_col))
                        q.append((n_row, n_col))
            return length


        
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                
                if  grid[i][j]==1 and (i,j) not in visited:
                    # print("Hello")
                    res.append(bfs(i,j))
        if res:
            return max(res)
        else: 
            return 0
        