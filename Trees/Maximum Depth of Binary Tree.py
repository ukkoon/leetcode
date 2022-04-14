from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:                
        if root == None:
            return 0

        left = self.maxDepth(root=root.left)
        right = self.maxDepth(root=root.right)

        depth = 1 + max(left,right)

        return depth