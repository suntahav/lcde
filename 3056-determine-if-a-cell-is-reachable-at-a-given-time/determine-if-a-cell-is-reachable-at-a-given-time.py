class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_diff = abs(fx - sx)
        y_diff = abs(fy - sy)
        MAX = max(x_diff, y_diff)
        MIN = min(x_diff, y_diff)
        
        if MAX == 0:
            if t == 1:
                return False
        if t >= MAX :
            return True
        return False