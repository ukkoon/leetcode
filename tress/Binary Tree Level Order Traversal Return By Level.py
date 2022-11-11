from operator import le
from queue import Queue
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        row = {}
        q = Queue()
        q.put({'level':0,
                'node':root})

        while not q.empty():
            cur = q.get()
            level = cur['level']
            node = cur['node']

            if cur and node:                                                
                if level not in row.keys():
                    row[level]=[]
                row[level].append(node.val)
                q.put({'level':level+1,
                    'node':node.left})                
                q.put({'level':level+1,
                    'node':node.right})
            
        return list(row.values())

# t=None
# t= TreeNode(val=1)
t = TreeNode(val=1,left=TreeNode(2,right=TreeNode(5)),right=TreeNode(3,left=TreeNode(6),right=TreeNode(7)))
t= TreeNode(val=1)
# t = TreeNode(val=1,left=TreeNode(2,left=TreeNode(3,left=TreeNode(4,left=TreeNode(5)))))
print(Solution().levelOrder(t))