# from collections import Counter
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if len(s) <=2:
        #     return True
        # counter = 0
        # left = 0
        # right = len(s)-1
        # cache_left = None
        # cache_right = None
        # while left < right:
        #     if s[left] == s[right]:
        #         left +=1
        #         right -=1
        #     else:
        #         counter += 1
        #         if counter == 2:
        #             left = cache_left
        #             right = cache_right
        #             right -= 1
        #             continue
        #         if counter > 2:
        #             return False
        #         cache_left = left
        #         cache_right = right
        #         left += 1
        # return True

        #### Better Solution

        left = 0
        right = len(s)-1

        while left <= right:
            if s[left] != s[right]:
                first = s[:left]+s[left+1:]
                second = s[:right] + s[right+1:]
                return first == first[::-1] or second == second[::-1]
            left += 1
            right -=1
        return True
