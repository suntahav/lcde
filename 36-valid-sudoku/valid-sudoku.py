class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
              e = board[i][j]
              if e == '.':
                continue
              if e in rows[i] or e in cols[j] or e in box[(i//3,j//3)]:
                return False
              else:
                rows[i].add(e)
                cols[j].add(e)
                box[(i//3,j//3)].add(e)
        return True
    