class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        #create a matrix map to track the location being visited
        mat_map = [[0]*n for i in range(m)]

        def search(row, col, current_word):
            #check index validity:
            if (row not in range(m)) or (col not in range(n)):
                return False

            #if already visited:
            if mat_map[row][col] == 1:
                return False
            else:
                mat_map[row][col] = 1

            #Create the new current word
            current_word = current_word + board[row][col]
            
            #base case when the word matches
            if current_word == word:
                return True

            #if the current index doesn't matches
            if len(current_word) < len(word):
                #Handle the cases
                #case when the new word index position doesnt match
                if current_word != word[:len(current_word)]:
                    #set the map locn false and backtrack
                    mat_map[row][col] = 0
                    return False
                #Now the new position index matches
                #check left
                left = search(row, col-1, current_word)
                if left:
                    return True
                #check right
                right = search(row, col+1, current_word)
                if right:
                    return True
                #check top
                top = search(row-1, col, current_word)
                if top:
                    return True
                #check bottom
                bottom = search(row+1, col, current_word)

                if bottom:
                    return True
                else:
                    mat_map[row][col] = 0
                    return False
            else:
                mat_map[row][col] = 0
                return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    #callfunc for search
                    res = search(i, j, '')
                    if res:
                        return True
        return False