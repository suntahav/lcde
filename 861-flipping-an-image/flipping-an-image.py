class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def xorify(num):
            return num ^ 1
        res = []
        for row in image:
            mod_row = list(map(xorify, row))[::-1]
            res.append(mod_row)
        return res
        