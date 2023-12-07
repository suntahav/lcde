class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #rows
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                row.append(board[i][j])
                col.append(board[j][i])
            rc = collections.Counter(row)
            cc = collections.Counter(col)
            r_c = rc.most_common(2)
            c_c = cc.most_common(2)
            if r_c[0][0] == '.':
                if len(r_c)>1 and r_c[1][1] > 1:
                    return False
            else:
                if r_c[0][1] > 1:
                    return False
            
            if c_c[0][0] == '.':
                if len(c_c) > 1 and c_c[1][1] > 1:
                    return False
            else:
                if c_c[0][1] > 1:
                    return False
        for r in range(3):
          for c in range(3):
            box = []
            for j in range(r*3,3*(r+1)):
              for k in range(c*3,3*(c+1)):
                box.append(board[j][k])
            counter = collections.Counter(box)
            r_c = counter.most_common(2)
            # print(r_c)
            if r_c[0][0] == '.':
                if len(r_c)>1 and r_c[1][1] > 1:
                    return False
            else:
                if r_c[0][1] > 1:
                    return False

        return True

# [[".",".",".",".","5",".",".","1","."],
#  [".","4",".","3",".",".",".",".","."],
#  [".",".",".",".",".","3",".",".","1"],
#  ["8",".",".",".",".",".",".","2","."],
#  [".",".","2",".","7",".",".",".","."],
#  [".","1","5",".",".",".",".",".","."],
#  [".",".",".",".",".","2",".",".","."],
#  [".","2",".","9",".",".",".",".","."],
#  [".",".","4",".",".",".",".",".","."]]        