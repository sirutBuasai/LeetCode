class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def order(list1, tree):
          if not tree:
            return
          
          order(list1, tree.left)
          order(list1, tree.right)
          list1.append(tree.val)
          
        result = []
        order(result, root)
        return result
      
