from typing import List, Optional
from Trees.TreeNode import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traversal(root,[])

    def traversal(self,root: Optional[TreeNode], q:List[int]):        
        if root is not None:
            q.append(root.val)       
            self.traversal(root.left,q)
            self.traversal(root.right,q)     
            return q   