# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # deph per node, and the root diameter is the sum of both depths 
        self.res = 0

        def dfs(root):
            

            if not root:
                return 0
            left  = dfs(root.left)
            right = dfs(root.right)
            # res is a global variable 
            self.res = max(self.res, left + right) # update with the depth or the combination 

            return 1 + max(left, right) 

        dfs(root)
        return self.res