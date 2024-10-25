from collections import deque

def adjacentToBoth(i, j, n, m):
    
    return (i, j) == (0, 0) or (i, j) == (n - 1, 0) or (i, j) == (n - 1, m - 1) or (i, j) == (0, m - 1)

def bfs(starts, heights, n, m):
    reachable = set(starts)
    q = deque(starts)
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Right, Down, Up, Left
    
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in reachable and heights[nx][ny] >= heights[x][y]:
                reachable.add((nx, ny))
                q.append((nx, ny))
    return reachable

def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []
    
    n, m = len(heights), len(heights[0])
    
    pacific_starts = [(0, j) for j in range(m)] + [(i, 0) for i in range(n)]
    atlantic_starts = [(n - 1, j) for j in range(m)] + [(i, m - 1) for i in range(n)]
    
    pacific_reachable = bfs(pacific_starts, heights, n, m)
    atlantic_reachable = bfs(atlantic_starts, heights, n, m)
    
  
    result = list(pacific_reachable & atlantic_reachable)
    return result
