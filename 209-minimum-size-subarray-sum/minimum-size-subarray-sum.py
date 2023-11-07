class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = 1000000000000000000
        left = 0
        right = 1
        LEN = len(nums)
        temp_sum = sum(nums[left:right]) 
        while left <= right and right <= LEN:
            # print(left, right, temp_sum)
            
            if temp_sum >= target:
                if min_len > (right - left):
                    min_len = right - left
                
            if temp_sum >= target:
                temp_sum -= nums[left]
                left += 1
            else:
                if right < LEN:
                    temp_sum += nums[right]
                right += 1
        if min_len == 1000000000000000000:
            min_len = 0
        return min_len

        