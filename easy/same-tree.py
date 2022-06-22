class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_queue = []
        q_queue = []

        p_queue.append(p)
        q_queue.append(q)

        while p_queue and q_queue:
          p_node = p_queue.pop(0)
          q_node = q_queue.pop(0)

          if p_node and q_node:
            if p_node.val != q_node.val:
              return False

            p_queue.append(p_node.left)
            q_queue.append(q_node.left)
            p_queue.append(p_node.right)
            q_queue.append(q_node.right)

          elif p_node or q_node:
              return False

        return p_queue == [] and q_queue == []
