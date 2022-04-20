from queue import Queue
from typing import List, Optional
from TreeNode import TreeNode


# Using Level Order Traversal.

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.levelOrder(root.left) == self.levelOrder(root.right,reversed=True)
    
    def levelOrder(self, root: Optional[TreeNode],reversed=False) -> List[int]:        
        visited = []        
        q = Queue()

        if root is not None:
            q.put(root)

        while not q.empty():
            cur = q.get()
            if cur is None:
                visited.append(None)
            else:
                visited.append(cur.val)
                if reversed:
                    q.put(cur.left)        
                    q.put(cur.right)

                else:
                    q.put(cur.right)
                    q.put(cur.left)
            
        return visited          

# Refernce beautiful code
# Using recursion

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.mirror(root,root)
        
    
    def mirror(self,n1,n2):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False
        
        return (n1.val == n2.val) and self.mirror(n1.left,n2.right) and self.mirror(n1.right, n2.left)
