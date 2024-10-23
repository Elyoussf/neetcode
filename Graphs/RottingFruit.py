from collections import deque

def orangesRotting(grid):
    q = deque()
    n = len(grid)
    m = len(grid[0])
    minutes = 0
    fresh_oranges = 0

    # First, find all the rotten oranges and count fresh ones
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:  # Rotten orange
                q.append((i, j))
            elif grid[i][j] == 1:  # Fresh orange
                fresh_oranges += 1

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # BFS to spread the rot
    while q and fresh_oranges > 0:
        # Process one level of rotten oranges (those that rot in this minute)
        for _ in range(len(q)):  # This ensures that we only process the current level
            px, py = q.popleft()
            for dx, dy in directions:
                nx, ny = px + dx, py + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:  # Fresh orange found
                    grid[nx][ny] = 2  # Rot this orange
                    fresh_oranges -= 1  # One less fresh orange
                    q.append((nx, ny))  # Add this newly rotten orange to the queue
        
        # After processing all oranges for this minute, increase the time
        minutes += 1

    # If there are still fresh oranges left, return -1
    return minutes if fresh_oranges == 0 else -1

# Test grid
grid = [[1,1,0],[0,1,1],[0,1,2]]

print(orangesRotting(grid))
