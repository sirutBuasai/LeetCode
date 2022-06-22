class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(tree, depth):
          if not tree or ((not tree.left) and (not tree.right)):
            return depth

          depth += 1
          if tree.left and tree.right:
            return min(dfs(tree.left, depth), dfs(tree.right,depth))
          elif not tree.left:
            return dfs(tree.right, depth)
          elif not tree.right:
            return dfs(tree.left, depth)

        if not root:
          return 0
        else:
          return dfs(root, 1)
