# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = root
        
        def bfs(root): 
            stack = deque()
            stack.append(root)
            while len(stack)>0:
                cn = stack.pop()
                if cn.val >= min(p.val,q.val) and cn.val <= max(p.val,q.val):
                    self.ans = cn
                    return        
                if cn.left:
                    stack.append(cn.left)
                if cn.right:
                    stack.append(cn.right)
        bfs(root)
        return self.ans