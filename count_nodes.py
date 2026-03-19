class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        if not root:
            return 0

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)

