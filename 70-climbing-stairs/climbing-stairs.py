class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        one = 1
        two = 2
        
        for i in range(3, n+1):
            temp = one + two
            one = two
            two = temp
        return two