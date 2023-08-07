class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        while lp < rp:
            mid = (lp + rp) // 2

            if mid == lp:
                break
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[lp] < target:
                    rp = mid
                elif nums[lp] > target:
                    if nums[lp] > nums[mid]:
                        rp = mid
                    else:
                        lp = mid
                else:
                    return lp
            else:
                if nums[rp] > target:
                    lp = mid
                elif nums[rp] < target:
                    if nums[rp] < nums[mid]:
                        lp = mid
                    else:
                        rp = mid
                else:
                    return rp
        if nums[lp] == target:
            return lp
        elif nums[rp] == target:
            return rp
        else:
            return -1