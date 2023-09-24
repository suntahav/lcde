class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        calc = (len(nums) * (0 + len(nums) + 1))// 2
        return calc - total
        