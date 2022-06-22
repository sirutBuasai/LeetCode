class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        d = {}
        q = []
        q.append(node)
        while q:
            curr = q.pop(0)
            if curr not in d:
                d[curr] = Node(curr.val)
            for n in curr.neighbors:
                if n not in d:
                    d[n] = Node(n.val)
                    q.append(n)
                d[curr].neighbors.append(d[n])

        return d[node]
