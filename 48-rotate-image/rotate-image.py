class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def calculate(left, right, matrix):
            if left == right :
                return
            if right - left == 1:
                temp = matrix[left][left]
                matrix[left][right], temp = temp, matrix[left][right]
                matrix[right][right], temp = temp, matrix[right][right]
                matrix[right][left], temp = temp, matrix[right][left]
                matrix[left][left] = temp
                return
            for i in range(left, right):
                temp = matrix[i][right]
                matrix[i][right] = matrix[left][i]
                temp,  matrix[right][right-i + left] = matrix[right][right - i+left], temp
                matrix[right-i+left][left], temp = temp, matrix[right-i+left][left]
                matrix[left][i] = temp
            return calculate(left + 1, right - 1, matrix)
        r = len(matrix[0])
        calculate(0, r-1, matrix)