class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # temp = [[-1001]*len(matrix) for i in range(len(matrix))]
        temp = []
        l = len(matrix)
        for col in range(len(matrix)):
            r = []
            for row in range(len(matrix)):
                r.append(matrix[row][col])
            temp.append(r[::-1])
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                matrix[row][col] = temp[row][col]
        