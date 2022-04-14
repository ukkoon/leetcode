class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        return b.count('1')

    def hammingWeight2(self, n: int) -> int:
        
        result = 0
        while n:            
            if n % 2 > 0:
                result+=1    
            n = n>>1
        return result