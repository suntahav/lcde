class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INT_MAX = 2**31
        LEN = len(coins)
        matrix = [[0] * (amount+1) for i in range(LEN+1)]

        for i in range( amount+1):
            matrix[0][i] = INT_MAX
        for i in range(1, amount+1):
            if i%coins[0] == 0:
                matrix[1][i] = i // coins[0]
            else:
                matrix[1][i] = INT_MAX
        
        for i in range(1, LEN+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    matrix[i][j] = min(matrix[i][j-coins[i-1]] + 1, matrix[i-1][j])
                else:
                    matrix[i][j] = matrix[i-1][j]
        if matrix[LEN][amount] >= INT_MAX:
            return -1
        return matrix[LEN][amount]
