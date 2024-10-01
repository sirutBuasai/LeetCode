class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_height(tree):
            if not tree:
                return 0

            left = find_height(tree.left)
            right = find_height(tree.right)

            return max(left, right) + 1

        return find_height(root)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        depth = 0

        while queue:
            node_level = len(queue)

            for _ in range(node_level):
                temp = queue.pop(0)

                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)

            depth += 1

        return depth
