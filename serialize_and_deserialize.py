from typing import TreeNode       

class Codec:

    def serialize(self, root):
        vals = []

        def dfs(node):
            if not node:
                vals.append("null")
                return
            
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "null":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            
            node.left = dfs()
            node.right = dfs()
            
            return node

        return dfs()