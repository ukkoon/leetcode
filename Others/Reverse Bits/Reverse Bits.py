class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n,'032b')
        rb = b[::-1]
        return int(rb,2)