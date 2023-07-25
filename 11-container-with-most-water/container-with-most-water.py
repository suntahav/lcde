class Solution:
    def calculate_vol(self, i_1, i_2, j_1, j_2):
        return min(j_1, j_2) * abs(i_1 - i_2)

    def maxArea(self, height: List[int]) -> int:
        l_p = 0
        r_p = len(height) - 1
        max_vol = 0
        while l_p < r_p:
            vol = self.calculate_vol(l_p, r_p, height[l_p], height[r_p])
            if vol > max_vol:
                max_vol = vol
            if height[l_p] < height[r_p]:
                l_p += 1
            else:
                r_p -= 1
        return max_vol