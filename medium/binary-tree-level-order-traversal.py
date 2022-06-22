class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        q.append(root)
        res = []

        while q:
            curr_lvl = []
            lvl_len = len(q)
            for _ in range(lvl_len):
                curr_node = q.pop(0)
                if curr_node:
                    curr_lvl.append(curr_node.val)
                    if curr_node.left:
                        q.append(curr_node.left)
                    if curr_node.right:
                        q.append(curr_node.right)
            if curr_lvl:
                res.append(curr_lvl)

        return res
