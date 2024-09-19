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


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        temp = root
        stack = [temp]

        if not temp:
          return None

        while stack:
            top = stack.pop()
            top.left, top.right = top.right, top.left

            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)

        return root
