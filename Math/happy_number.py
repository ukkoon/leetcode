from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:                
        """
        mathmatial한 문제인 줄 알았는데, 사실 그것보다는
        긴 정수의 각 자릿수를 구하는 로직에 풀이의 핵심이 담겨있는 문제였다.
        일반적으로 접근하는 reduce(str(n))방식은 성능이 비싸다.        
        """
        memory = set()        
        
        while n not in memory:
            copy = n
            sum = 0 
            while copy > 0:                                
                sum += pow(copy%10,2)
                copy = copy//10

            if sum == 1:
                return True
            else:
                memory.add(n)
                n = sum

        return False


print(Solution().isHappy(3232))