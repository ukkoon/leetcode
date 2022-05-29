class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 1 :
            n /= 3
            if n==1:
                return True
        return False




# 3^20 === True
print(Solution().isPowerOfThree(n=3486784401))
