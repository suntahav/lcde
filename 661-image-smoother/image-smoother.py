class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROW = len(img)
        COL = len(img[0])
        res = []
        for i in range(ROW):
            temp = []
            for j in range(COL):
                a = 0
                c = 0
                if i-1 in range(ROW):
                    if j-1 in range(COL):
                        a += img[i-1][j-1]
                        c += 1
                    a += img[i-1][j]
                    c += 1
                    if j+1 in range(COL):
                        a+= img[i-1][j+1]
                        c += 1
                if i+1 in range(ROW):
                    if j-1 in range(COL):
                        a += img[i+1][j-1]
                        c += 1
                    a += img[i+1][j]
                    c += 1

                    if j+1 in range(COL):
                        a+= img[i+1][j+1]
                        c += 1
                if j-1 in range(COL):
                    a += img[i][j-1]
                    c += 1
                a += img[i][j]
                c += 1
                if j+1 in range(COL):
                    a+= img[i][j+1]
                    c += 1
                temp.append(a//c)
            res.append(temp)
        return res

                

        