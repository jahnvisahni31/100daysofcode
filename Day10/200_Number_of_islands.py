class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:  #if grid is not there then return 0
            return 0

        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':     #return a empty when i , j are values in negative and grid[i][j] == 0
                return
            grid[i][j] = '0'
            dfs(grid, i + 1, j)    #return all cases of dfs traversal
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        num_islands = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):           #when grid is 1 then it may increase by 1 and then return the function of dfs that makes sure that all the case satisfy and it returns the value of number of islands
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(grid, i, j)
        return num_islands
        
