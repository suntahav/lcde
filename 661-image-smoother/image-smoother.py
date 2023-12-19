class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROW = len(img)
        COL = len(img[0])
        ROW_R = range(ROW)
        COL_R = range(COL)
        res = []
        for i in ROW_R:
            temp = []
            for j in COL_R:
                a = 0
                c = 0
                if i-1 in ROW_R:
                    if j-1 in COL_R:
                        a += img[i-1][j-1]
                        c += 1
                    a += img[i-1][j]
                    c += 1
                    if j+1 in COL_R:
                        a+= img[i-1][j+1]
                        c += 1
                if i+1 in ROW_R:
                    if j-1 in COL_R:
                        a += img[i+1][j-1]
                        c += 1
                    a += img[i+1][j]
                    c += 1

                    if j+1 in COL_R:
                        a+= img[i+1][j+1]
                        c += 1
                if j-1 in COL_R:
                    a += img[i][j-1]
                    c += 1
                a += img[i][j]
                c += 1
                if j+1 in COL_R:
                    a+= img[i][j+1]
                    c += 1
                temp.append(a//c)
            res.append(temp)
        return res

                

        