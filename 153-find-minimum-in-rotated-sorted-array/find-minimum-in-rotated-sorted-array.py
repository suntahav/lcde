class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp < rp:
            mid = (lp + rp) // 2
            if mid == lp:
                break
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[rp]:
                lp = mid
            else:
                rp = mid
        return min(nums[lp], nums[rp])