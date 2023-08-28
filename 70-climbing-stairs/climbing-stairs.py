class Solution:
    def climbStairs(self, n: int) -> int:
        # mem = [0]*(n+1)
        # mem[0] = 1
        # for i in range(1,n+1):
        #     mem[i] += mem[i-1]
        #     if i-2 >= 0:
        #         mem[i] += mem[i-2] 
            
        # return mem[n]
        pre = 1
        cur = 1
        for i in range(1, n):
            temp = cur+pre
            pre = cur
            cur = temp
        return cur
