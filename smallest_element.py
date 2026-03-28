from typing import Optional, List, TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val
            curr = curr.right     



