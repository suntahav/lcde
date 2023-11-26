class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        LEN = len(digits)
        carry = 0
        carry = (digits[LEN-1] + 1)//10
        digits[LEN-1] = (digits[LEN-1] + 1)%10
        i = LEN - 2
        while i >= 0:
            if carry == 0:
                break
            new_carry = (digits[i] + carry)//10
            digits[i] = (digits[i] + carry)%10
            carry = new_carry
            i -= 1
        if carry != 0 :
            digits.insert(0, carry)
        return digits
            

        