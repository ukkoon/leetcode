# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:        
        left = 1
        right = n

        while left<=right:
            mid = (left+right)//2
            if not self.isBadVersion(mid-1) and self.isBadVersion(mid):
                return mid
            elif self.isBadVersion(mid-1) and self.isBadVersion(mid):                
                right = mid-1                            
            else :
                left = mid+1 
                
                                
    def isBadVersion(self,version:int)->bool:
        return version>7

print(Solution().firstBadVersion(n=10))