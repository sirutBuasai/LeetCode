class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(tree, arr):
          if not tree:
            return
          dfs(tree.left, arr)
          arr.append(tree.val)
          dfs(tree.right, arr)
          
        result = []
        dfs(root, result)
        return result
        
