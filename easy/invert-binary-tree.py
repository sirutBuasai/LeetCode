class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
          return None

        else:
          temp = root.left
          root.left = root.right
          root.right = temp

          self.invertTree(root.left)
          self.invertTree(root.right)

        return root
