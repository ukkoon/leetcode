class Solution:
    def climbStairs(self, n: int) -> int:
        caches = [0] * n
        caches [0:2] = [1,2,3]
        
        for i in range(3,n):
            caches [i] = caches[i-1]+caches[i-2]
        
        return caches[n-1]
            