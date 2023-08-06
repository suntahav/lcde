class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp < rp:
            mid = (lp + rp) // 2
            if mid == lp:
                break
            #if immediate next of mid less than mid then that is least due to flip
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # if mid is greater than rp means a flip somewhere in between so move lp ahead
            elif nums[mid] > nums[rp]:
                lp = mid
            # if mid is less than rp means it behaves as normal ascending array so less element should be before hence move rp to mid
            else:
                rp = mid
            # return min in case mid becomes equal to lp
        return min(nums[lp], nums[rp])