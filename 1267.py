class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        serverRows = {}
        serverCols = {}

        m = len(grid)
        n = len(grid[0])

        # add servers to existence map
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    if (i in serverRows):
                        serverRows[i] += 1
                    else:
                        serverRows[i] = 1
                    
                    if (j in serverCols):
                        serverCols[j] += 1
                    else:
                        serverCols[j] = 1
        
        overlapServers = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    if (serverRows[i] >= 2 or serverCols[j] >= 2):
                        overlapServers += 1
        
        return overlapServers