class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[-1]*(k+1) for i in range(n+1)]

        def solve(k, n):
            if n==0 or n==1:
                return n
            if k==1:
                return n
            if dp[n][k] != -1:
                return dp[n][k]
            res = 10000000000
            left = 1
            right = n

            while left <= right:
                mid = (left + right)//2
                t1 = solve(k, n-mid)
                t2 = solve(k-1, mid-1)
                temp = 1+max(t1, t2)
                if t1 > t2:
                    left = mid+1
                else:
                    right = mid-1
                res = min(res, temp)
            dp[n][k] = res
            return res
        return solve(k, n)



        