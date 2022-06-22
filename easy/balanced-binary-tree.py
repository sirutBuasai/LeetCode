class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find_height(tree):
            if not tree:
                return 0
            return max(find_height(tree.left), find_height(tree.right)) + 1

        def find_balance(tree):
            if not tree:
                return True

            return abs(find_height(tree.left) - find_height(tree.right)) <= 1 and find_balance(tree.left) and find_balance(tree.right)

        return find_balance(root)
