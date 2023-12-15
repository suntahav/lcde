class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = str(x)[1:]
            s = s[::-1]
            s = '-'+s
            s = int(s)
            if s < -2**31:
                return 0
        else:
            s = str(x)
            s = s[::-1]
            s = int(s)
            if s > 2**31-1:
                return 0
        return s