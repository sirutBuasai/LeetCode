class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def find_height(tree):
            if not tree:
                return 0

            left = find_height(tree.left)
            right = find_height(tree.right)
            ans[0] = max(ans[0], left+right)

            return max(left, right) + 1

        find_height(root)
        return ans[0]
