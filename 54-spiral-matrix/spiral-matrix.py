class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        directions = [0, 1, 0, -1, 0]  # right, down, left, up pairs
        visited = [[False] * cols for _ in range(rows)]
        row, col, dir_idx = 0, 0, 0
        result = []
        for _ in range(rows * cols):
            result.append(matrix[row][col])
            visited[row][col] = True
            nr = row + directions[dir_idx]
            nc = col + directions[dir_idx + 1]
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or visited[nr][nc]:
                dir_idx = (dir_idx + 1) % 4
            row += directions[dir_idx]
            col += directions[dir_idx + 1]
        return result

        