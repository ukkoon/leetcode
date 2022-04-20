from typing import Optional
from Trees.TreeNode import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:                
        if root is None:
            return 0

        left = self.maxDepth(root=root.left)
        right = self.maxDepth(root=root.right)

        depth = 1 + max(left,right)

        return depth