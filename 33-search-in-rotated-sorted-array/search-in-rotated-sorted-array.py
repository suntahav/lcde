class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        while lp < rp:
            mid = (lp + rp) // 2
            #we are at the element or not in any case finished
            if mid == lp:
                break
            # mid is target
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                #mid gt target but lp is less should be somewhere in between so move rp
                if nums[lp] < target:
                    rp = mid
                elif nums[lp] > target:
                    #mid & lp gt target but if mid is lt lp means flip in between so less value in between
                    if nums[lp] > nums[mid]:
                        rp = mid
                    # normal case of no flip and move lp
                    else:
                        lp = mid
                else:
                    #else lp is answer if equal
                    return lp
            else:
                #rp gt target and mid is less so shift lp to mid
                if nums[rp] > target:
                    lp = mid
                elif nums[rp] < target:
                    #both rp and mid less than target so flip in between so larger target in between
                    if nums[rp] < nums[mid]:
                        lp = mid
                    # regular case no flip
                    else:
                        rp = mid
                else:
                    # rp is target
                    return rp
        if nums[lp] == target:
            return lp
        elif nums[rp] == target:
            return rp
        else:
            #not found in array
            return -1