class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        LEN = len(coins)
        matrix = [[0]*(amount+1) for i in range(LEN+1)]
        for i in range(LEN+1):
            matrix[i][0] = 1
        for i in range(1, LEN+1):
            for j in range(amount+1):
                if coins[i-1] <= j:
                    matrix[i][j] = matrix[i][j-coins[i-1]] + matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j]
        return matrix[-1][-1]

        