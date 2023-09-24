class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        remaining_bits = 32 - len(binary)
        temp = ''
        for i in range(remaining_bits):
            temp+='0'
        return int(binary[::-1]+ temp, 2)
        