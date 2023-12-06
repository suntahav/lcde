class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        visit = set()

        def bfs(i,j):
            v = set()
            q = collections.deque()
            q.append((i,j))

            direction = [[1,0],[-1,0],[0,1],[0,-1]]

            while q:
                row, col = q.popleft()
                v.add((row, col))
                for r,c in direction:
                    n_r = r+row
                    n_c = c+col
                    if n_r in range(ROWS) and n_c in range(COLS):
                        if (n_r,n_c) not in v and board[n_r][n_c] == "O":
                          v.add((n_r, n_c))
                          q.append((n_r, n_c))
                    else:
                        return True, v
            return False, v
        safe = set()
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="O" and (i,j) not in visit:
                    edge, v = bfs(i,j)
                    if edge:
                        safe = safe.union(v)
                        continue
                    else:
                        for r,c in v:
                            board[r][c] = "X"
                        
        