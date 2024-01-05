class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            j = i-1
            temp = 0
            # dummy = False
            while j >= 0:
                if nums[j] < nums[i]:
                    temp = max(temp, dp[j])
                    j -= 1
                else:
                    j -=1
            dp[i] += temp
        return max(dp)
        