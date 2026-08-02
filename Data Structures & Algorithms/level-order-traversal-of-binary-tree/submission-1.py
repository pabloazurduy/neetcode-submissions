# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.levels = defaultdict(list)
        
        def bfs(root):
            q = deque()
            if root:
                q.append((0,root))
            while len(q)>0:
                l, cn = q.popleft()
                self.levels[l].append(cn.val)
                if cn.left:
                    q.append((l+1, cn.left))
                if cn.right:
                    q.append((l+1, cn.right))

        bfs(root)
        return list(self.levels.values())