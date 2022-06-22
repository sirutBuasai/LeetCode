class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      res = []
      stack = []
      curr = root
      while (stack or curr) and len(res) < k:
        if curr:
          stack.append(curr)
          curr = curr.left
        else:
          curr = stack.pop()
          res.append(curr.val)
          curr = curr.right

      return res[-1]
