# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # worst time alternative, for every node check if both tree's are the same 
        def is_equal(root_a, root_b):
            if root_a is None and root_b is None:
                return True 
            elif (root_a and root_b) and (root_a.val == root_b.val):
                return (is_equal(root_a.left, root_b.left) and 
                        is_equal(root_a.right, root_b.right))
            else:
                return False 
        
    
        if is_equal(root, subRoot):
            return True
        elif root and subRoot:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False 