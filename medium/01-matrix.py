class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row,col = len(mat), len(mat[0])
        out = [[float('inf') for _ in range(col)] for _ in range(row)]

        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    print(r,c)
                    out[r][c] = 0
                else:
                    if r > 0:
                        out[r][c] = min(out[r][c], out[r-1][c] + 1)
                    if c > 0:
                        out[r][c] = min(out[r][c], out[r][c-1] + 1)

        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                if r < row-1:
                    out[r][c] = min(out[r][c], out[r+1][c] + 1)
                if c < col-1:
                    out[r][c] = min(out[r][c], out[r][c+1] + 1)

        return out
