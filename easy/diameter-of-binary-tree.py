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


class Solution:
    def __init__(self) -> None:
        self.diameter = 0

    def find_height(self, tree) -> int:
        if not tree:
            return 0
        left = self.find_height(tree.left)
        right = self.find_height(tree.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.find_height(root)
        return self.diameter
