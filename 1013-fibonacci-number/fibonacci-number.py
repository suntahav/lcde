class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        # return self.fib(n-1) + self.fib(n-2)
        prev_0 = 0
        prev_1 = 1
        for i in range(2, n+1):
            prev_0, prev_1 = prev_1, prev_0 + prev_1
        return prev_1

        