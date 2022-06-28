class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree, lower, upper):
            if not tree:
                return True

            if lower < tree.val and tree.val < upper:
                return dfs(tree.left, lower, tree.val) and dfs(tree.right, tree.val, upper)
            else:
                return False

        return dfs(root, float('-inf'), float('inf'))
