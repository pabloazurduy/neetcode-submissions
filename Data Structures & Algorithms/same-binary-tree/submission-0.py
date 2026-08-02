# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p_root, q_root):
            if p_root is None and q_root is None:
                return 
            elif (p_root and q_root) and p_root.val == q_root.val:
                dfs(p_root.left, q_root.left)
                dfs(p_root.right, q_root.right)                
            else:
                raise ValueError('non equal') 
        try:
            dfs(p,q)
        except ValueError:
            return False
        return True
