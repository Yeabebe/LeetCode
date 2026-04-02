from typing import TreeNode  

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case
        if not root or root == p or root == q:
            return root
        
        # Search in left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both sides found something → this is LCA
        if left and right:
            return root
        
        # Otherwise return the non-null side
        return left if left else right