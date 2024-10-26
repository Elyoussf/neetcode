from collections import deque

class Solution:
    def solve(self, board) -> None:
        n = len(board)
        m = len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = {}  # Store visited cells

        def bfs(ox, oy):
            tempQueue = deque([(ox, oy)])
            group = []
            notValidGroup = False

            while tempQueue:
                nox, noy = tempQueue.popleft()
                if visited.get((nox, noy), False):
                    continue
                visited[(nox, noy)] = True
                group.append((nox, noy))

                # If any cell in the group is on the border, mark the group as invalid
                if nox == 0 or nox == n - 1 or noy == 0 or noy == m - 1:
                    notValidGroup = True

                for dx, dy in directions:
                    nx, ny = nox + dx, noy + dy
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'O' and not visited.get((nx, ny), False):
                        tempQueue.append((nx, ny))

            # Only flip cells if the group is valid (fully surrounded by 'X')
            if not notValidGroup:
                for x, y in group:
                    board[x][y] = 'X'

        # Traverse the board to find all 'O' cells and apply BFS if not visited
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not visited.get((i, j), False):
                    bfs(i, j)


