from typing import List, Optional
from Trees.TreeNode import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traversal(root,[])

    def traversal(self,root: Optional[TreeNode], q:List[int]):        
        if root is not None: 
            self.traversal(root.left,q)    
            self.traversal(root.right,q)
            q.append(root.val)              
            return q   