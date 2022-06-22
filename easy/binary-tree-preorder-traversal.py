class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def order(list1, tree):
          if not tree:
            return
          list1.append(tree.val)
          order(list1, tree.left)
          order(list1, tree.right)

        result = []
        order(result, root)
        return result
