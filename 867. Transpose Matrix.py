def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    rows, cols = len(matrix), len(matrix[0])
    r = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            r[j][i] = matrix[i][j]
    return r