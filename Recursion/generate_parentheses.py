from typing import List
import itertools


mapping = {1:"(", 0:")"}
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        slow solution
        """
        bins = list(map(list, itertools.product([0, 1], repeat=n*2)))
        bins = list(filter(lambda x:True if x.count(1)==n else False,bins))
        
        result = []
        for bin in bins:
            if self.isParenthesis(bin):
                result.append(''.join(list(map(lambda x:mapping[x],bin))))
        return result
        
    def isParenthesis(self, bin:List[int]):
        stack = [*bin]
        left = []
        right = []
        
        while stack:
            if stack.pop(0) == 1:
                left.append(1)
            else:
                right.append(0)
            if len(right)>len(left):
                return False
                          
        return True
        

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        backtracking solution
        """
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans

Solution().generateParenthesis(8)