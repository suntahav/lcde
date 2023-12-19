class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INT_MAX = 2**32
        LEN = len(coins)
        t = [[-1]*(amount+1) for i in range(LEN+1)]

        # for i in range(LEN+1):
        #     t[i][0] = 0
        for i in range(amount+1):
            t[0][i] = INT_MAX
        for i in range(amount+1):
            if i %coins[0]==0:
                t[1][i] = i // coins[0]
            else:
                t[1][i] = INT_MAX
        for i in range(LEN+1):
            t[i][0]=0
        for i in range(2, LEN+1):
            for j in range(1,amount+1):
                if coins[i-1] <= j:
                    t[i][j] = min(t[i-1][j], 1+t[i][j-coins[i-1]])
                else:
                    t[i][j] = t[i-1][j]
        if t[LEN][amount] >= 2**32:
            return -1
        return t[LEN][amount]
        