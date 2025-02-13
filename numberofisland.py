class Solution(object):
    def numIslands(self, grid):
        res=0
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j,row,col)
                    res=res+1
        return res
    def dfs(self,grid,i,j,row,col):
        if i<0 or j<0 or i>=row or j>=col or grid[i][j]=='0':
            return
        grid[i][j]='0'
        self.dfs(grid,i+1,j,row,col)
        self.dfs(grid,i-1,j,row,col)
        self.dfs(grid,i,j+1,row,col)
        self.dfs(grid,i,j-1,row,col)
