class Solution:
    def trap(self, height: List[int]) -> int:
        max_val = max(height)
        m = [0]
        for i in range(len(height)):
            if height[i] == max_val:
                m.append(i)

        def solve(height):
            cur_max = 0
            res = 0
            temp_res = 0
            flag = True
            for h in height:
                if h < cur_max:
                    temp_res += cur_max-h
                    continue
                if h >= cur_max:
                    cur_max = h
                    res += temp_res
                    temp_res = 0
                    continue
            return res
        final_res = 0
        for i in range(1,len(m)):
            final_res += solve(height[m[i-1]:m[i]+1])
        final_res += solve(list(height[m[len(m)-1]:])[::-1])
        return final_res
            
        