class Solution:
    def divide(self, dividend: int, divisor: int) -> int:        
        dividend_negative = False
        divisor_negative = False
        if dividend <0:
            dividend_negative =True
            dividend = -dividend

        if divisor<0:
            divisor_negative = True
            divisor = -divisor
        
        result = 1
        while dividend>divisor:
            # print(f"{dividend} > {divisor}")
            dividend>>=1
            result*=2
        print(f'dividend:{dividend}')
        
    
        return -result if divisor_negative else result

# print(Solution().divide(dividend=-2147483648,divisor=-1))        
print(Solution().divide(dividend=8,divisor=3))        
print(Solution().divide(dividend=10,divisor=3)) 
print(Solution().divide(dividend=12,divisor=3))
print(Solution().divide(dividend=16,divisor=3))        
# print(Solution().divide(dividend=7,divisor=3))
# print(Solution().divide(dividend=7,divisor=-3))
# print(Solution().divide(dividend=1,divisor=1))
# print(Solution().divide(dividend=1,divisor=-1))