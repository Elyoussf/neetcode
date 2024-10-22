grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

def maxAreaIsland(grid):
    area=0
    n  = len(grid)
    m = len(grid[0])
    visited = {} #marks the visited cells 
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and not visited.get((i,j),False):
                
                
                area = max(area,countOnes(i,j,grid,visited))
    return area


def countOnes(i,j,grid ,visited ):
    if visited.get((i, j), False) or grid[i][j]==0:
        return 0 
    visited[(i,j)] = True
    a,b,c,d = 0,0,0,0
    if i+1<len(grid):
        a = countOnes(i+1,j,grid,visited)
    if i-1>=0:
        b = countOnes(i-1,j,grid,visited)
    if j+1<len(grid[0]):
        c = countOnes(i,j+1,grid,visited)
    if j-1>=0:
        d = countOnes(i,j-1,grid,visited)
    return 1+a+b+c+d


print(maxAreaIsland(grid))
    
