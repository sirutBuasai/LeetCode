class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Helper Functions -------------------------------
        def valid(matrix, x, y):
            return x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0])
        
        def neighbors(matrix, x, y):
            avail = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
            res = []
            for i, j in avail:
                if valid(matrix, i, j):
                    res.append((i,j))
            return res
        
        # Main Functions ---------------------------------
        visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
        island = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j]:
                    continue
                    
                elif grid[i][j] == "0":
                        visited[i][j] = True
                        continue
                
                else:
                    print(i, j)
                    island += 1
                    stack = [(i,j)]
                    while stack:
                        row, col = stack.pop(0)

                        if not visited[row][col]:
                            visited[row][col] = True

                            if grid[row][col] == '1':
                                for r, c in neighbors(grid, row, col):
                                    if not visited[r][c]:
                                        stack.append((r,c))

        return island
        
