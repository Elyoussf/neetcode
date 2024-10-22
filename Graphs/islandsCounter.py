islands = [
   ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
#dfs works here
def numberOfislands(grid ):
    start = (0,0)
    visited  = {} # tuple <==> boolean 
    n = len(grid)
    m = len(grid[0])
    counter = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="1" and not visited.get((i, j), False):
                MarkTheIsland(i,j,grid,visited)
                counter+=1
    return counter

#Here this function will iterate over the ilands here and marks them visited after tha completion it will increase the counter
def MarkTheIsland(i,j,grid,visited):
    if visited.get((i, j), False) or grid[i][j]=="0":
        return 
    visited[i,j] = True
    if i+1<len(grid):
        MarkTheIsland(i+1,j,grid,visited)
    if i-1>=0:
        MarkTheIsland(i-1,j,grid,visited)
    if j+1<len(grid[0]):
        MarkTheIsland(i,j+1,grid,visited)
    if j-1>=0:
        MarkTheIsland(i,j-1,grid,visited)
    
print(numberOfislands(islands))