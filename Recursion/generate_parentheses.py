import itertools
from typing import List

# mapping = {1:"(", 0:")"}
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         """
#         slow solution
#         """
#         bins = list(map(list, itertools.product([0, 1], repeat=n*2)))
#         bins = list(filter(lambda x:True if x.count(1)==n else False,bins))
        
#         result = []
#         for bin in bins:
#             if self.isParenthesis(bin):
#                 result.append(''.join(list(map(lambda x:mapping[x],bin))))
#         return result
        
#     def isParenthesis(self, bin:List[int]):
#         stack = [*bin]
#         left = []
#         right = []
        
#         while stack:
#             if stack.pop(0) == 1:
#                 left.append(1)
#             else:
#                 right.append(0)
#             if len(right)>len(left):
#                 return False
                          
#         return True
            
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def backtracking(left,right):
            if len(stack)==n*2:
                result.append(''.join(stack))
                return
            if left<n:
                stack.append("(")
                backtracking(left+1,right)
                stack.pop()
            if left>right:
                stack.append(")")
                backtracking(left,right+1)
                stack.pop()
        
        backtracking(0,0)                        
        return result
        

Solution().generateParenthesis(3)