class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dp = {}
        def solve(a,b):
            dpstr = a + "+"+b
            
            if dpstr in dp:
                return dp[dpstr]
            if sorted(a) != sorted(b):
                return False
            if len(a) != len(b):
                return False
                
            LEN = len(a)
            
            if LEN <1 :
                return False
                
            if LEN==1:
                if a==b:
                    return True
                else:
                    return False
            
            res = False
            for k in range(1, LEN):
                left = a[:k]
                right = a[k:]
                
                #No swap
                no_swap_left = solve(left, b[:k])
                no_swap_right = solve(right, b[k:])
                no_swap = no_swap_left and no_swap_right
                
                #swap
                swap_left = solve(left, b[LEN-k:])
                swap_right = solve(right, b[:LEN-k])
                swap = swap_left and swap_right
                
                res = no_swap or swap
                
                if res:
                    break
            dp[dpstr] = res
            # print(res)
            return res
            
        return solve(s1, s2)
           