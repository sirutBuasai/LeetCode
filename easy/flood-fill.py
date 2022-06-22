class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        old_color = image[sr][sc]
        image[sr][sc] = newColor

        def neighbors(r,c,grid):
            available = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            res = []
            for i, j in available:
                if valid(i,j,grid):
                    res.append((i,j))
            return res

        def valid(r,c, grid):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == old_color

        def dfs(curr_r, curr_c, visited, grid):
            visited.add((curr_r, curr_c))
            for nr, nc in neighbors(curr_r, curr_c, grid):
                if (nr, nc) not in visited:
                    grid[nr][nc] = newColor
                    dfs(nr, nc, visited, grid)



        dfs(sr, sc, visited, image)
        return image
