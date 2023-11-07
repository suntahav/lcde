class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # min_len = float('inf')
        # left = 0
        # right = 1
        # LEN = len(nums)
        # temp_sum = sum(nums[left:right]) 
        # while left <= right and right <= LEN:
        #     # print(left, right, temp_sum)
            
        #     if temp_sum >= target:
        #         if min_len > (right - left):
        #             min_len = right - left
                
        #     if temp_sum >= target:
        #         temp_sum -= nums[left]
        #         left += 1
        #     else:
        #         if right < LEN:
        #             temp_sum += nums[right]
        #         right += 1
        # if min_len == float('inf'):
        #     min_len = 0
        # return min_len

        total = 0
        left = 0
        right = 0
        LEN = len(nums)
        min_len = float("inf")
        while right < LEN and left <= right:
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right-left+1)
                total -= nums[left]
                left += 1
            right += 1
        
        if min_len == float("inf"):
            return 0
        return min_len

        