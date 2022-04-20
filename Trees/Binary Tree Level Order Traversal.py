from queue import Queue
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        visited = []        
        q = Queue()
        q.put(root)

        while not q.empty():
            cur = q.get()

            if cur is not None:                
                visited.append(cur.val)                
                q.put(cur.left)                
                q.put(cur.right)
            else:
                visited.append(None)
                
        return visited

# t=None
# t= TreeNode(val=1)
t = TreeNode(val=1,left=TreeNode(2,right=TreeNode(5)),right=TreeNode(3,left=TreeNode(6),right=TreeNode(7)))
print(Solution().levelOrder(t))