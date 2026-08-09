from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row= len(grid)
        col = len(grid[0])
        f_orange = 0
        rot = deque()
        # grid_c = deepcopy(grid)        
        for r in range(row):
            for c in range(col):
                if grid[r][c] ==1:
                    f_orange += 1
                elif grid[r][c] ==2:
                    rot.append([r, c])

        minute =0
        while len(rot) and f_orange >0:
            minute += 1
            for i in range(len(rot)):
                x, y = rot.popleft()
                for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                   
                    r = x + dx
                    c = y + dy
                    
                    if (0<= r < row and 0 <= c < col ) and  grid[r][c] == 1  :
                            grid[r][c] = 2
                            f_orange -= 1
                            rot.append([r , c])
        # print (grid_c)
        if f_orange > 0:
            return -1
        return minute






        