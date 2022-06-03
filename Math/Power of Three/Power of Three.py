class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 1 :
            if n==1:
                return True
            n /= 3
        return False




# 3^20 === True
print(Solution().isPowerOfThree(n=0))
