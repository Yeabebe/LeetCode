from typing import Optional, TreeNode               

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        total = 0

        # Check if the left child is a leaf
        if root.left:
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        # Traverse the right subtree
        total += self.sumOfLeftLeaves(root.right)

        return total