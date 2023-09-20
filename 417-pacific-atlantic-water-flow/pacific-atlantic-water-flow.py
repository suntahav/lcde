class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        grid_map = [[0]*COL for i in range(ROW)] #Memorize 

        def dfs(r, c, visited) -> (bool, bool):
            if grid_map[r][c] == 1:
                return True, True
            is_pacific, is_atlantic = False, False
            if (r == 0 or c == 0):
                is_pacific = True
            if (c == COL-1 or r == ROW-1):
                is_atlantic = True
            
            visited = visited + [(r, c)]
            #Check North
            if r >= 1:
                if heights[r-1][c] <= heights[r][c] and ((r-1,c) not in visited):
                    pac, atl = dfs(r-1, c, visited)
                    is_pacific = pac or is_pacific
                    is_atlantic = atl or is_atlantic
            if is_pacific and is_atlantic:
                grid_map[r][c] = 1
                return True, True
            #check South
            if r < ROW-1:
                if heights[r+1][c] <= heights[r][c] and ((r+1,c) not in visited):
                    pac, atl = dfs(r+1, c, visited)
                    is_pacific = pac or is_pacific
                    is_atlantic = atl or is_atlantic
            if is_pacific and is_atlantic:
                grid_map[r][c] = 1
                return True, True
            #Check East
            if c < COL-1:
                if heights[r][c+1] <= heights[r][c] and ((r,c+1) not in visited):
                    pac, atl = dfs(r, c+1, visited)
                    is_pacific = pac or is_pacific
                    is_atlantic = atl or is_atlantic
            if is_pacific and is_atlantic:
                grid_map[r][c] = 1
                return True, True
            #check West
            if c >= 1:
                if heights[r][c-1] <= heights[r][c] and ((r,c-1) not in visited):
                    pac, atl = dfs(r, c-1, visited)
                    is_pacific = pac or is_pacific
                    is_atlantic = atl or is_atlantic
                    
            if is_pacific and is_atlantic:
                grid_map[r][c] = 1

            return is_pacific, is_atlantic
        
        res = []
        
        for i in range(ROW):
            for j in range(COL):
                pacific, atlantic = dfs(i,j, [])
                if pacific and atlantic:
                    res.append([i,j])
        return res
        