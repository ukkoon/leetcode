class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        return self.isValid(root)

    def isValid(self,root,leftLimit=-math.inf,rightLimit=math.inf) -> bool:

        if not root:
            return True
            
        if leftLimit < root.val < rightLimit:
            leftOk = self.isValid(root.left,leftLimit=leftLimit,rightLimit=root.val)
            rightOk = self.isValid(root.right,leftLimit=root.val,rightLimit=rightLimit)
            return leftOk and rightOk
                    
        else:
            return False
                        
            
        
            