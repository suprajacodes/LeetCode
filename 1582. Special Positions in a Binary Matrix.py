class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        rc = [0] * rows
        cc = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    rc[i] += 1
                    cc[j] += 1

        res = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and rc[i] == 1 and cc[j] == 1:
                    res += 1
        return res

