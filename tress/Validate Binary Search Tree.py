import math
from typing import Optional
from Trees.TreeNode import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        return self.isValid(root)

    def isValid(self,root,leftLimit=-math.inf,rightLimit=math.inf) -> bool:
        if root is None:
            return True
            
        if leftLimit < root.val < rightLimit:
            leftOk = self.isValid(root.left,leftLimit,root.val)
            rightOk = self.isValid(root.right,root.val,rightLimit)
            
            return leftOk and rightOk
                    
        else:
            return False                        
            
        
            