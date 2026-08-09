class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        ans = 0
        grid_c = grid[:]
        def traverse( node , g=grid_c):
            x,y = node
            
            for i in [(0,1),(0,-1),(1,0),(-1,0)]:
                dx, dy = i
                r = x + dx
                c = y + dy                
                if (0<= r < row and  0 <= c <col) and g[r][c] == "1":
                    g[r][c] = "-1"
                    traverse((r,c))

        
        for i in range(row):
            for j in range(col):
                if grid_c[i][j] == "1":
                    grid_c[i][j] = "-1"
                    traverse((i,j))
                    ans += 1
        
        return ans




       