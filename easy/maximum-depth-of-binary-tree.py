class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_height(tree):
            if not tree:
                return 0

            left = find_height(tree.left)
            right = find_height(tree.right)

            return max(left, right) + 1

        return find_height(root)
