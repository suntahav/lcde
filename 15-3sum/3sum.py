class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        nums_dict = {}
        hash = set()
        res = []
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        for i in range(len(nums)-2):
            first_num = nums[i]
            remain_sum = -1 * nums[i]
            if i > 0 and nums[i-1] == first_num: # Critical part as again starting with prev number results in duplicate
                continue
            for j in range(i+1, len(nums)-1):
                second_num = nums[j]
                third_num = remain_sum - second_num
                if third_num < second_num:
                    continue
                if third_num in nums_dict:
                    counter = 1
                    if third_num == first_num:
                        counter += 1
                    if third_num == second_num:
                        counter += 1
                    if nums_dict[third_num] >= counter:
                        temp_res = [first_num, second_num, third_num]
                        dummy =  ''.join(str(x)+' ' for x in temp_res)
                        if dummy not in hash:
                            hash.add(dummy)
                            res.append(temp_res)
        return res