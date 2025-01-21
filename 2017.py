class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # define prefix sum lists: r1, r2 (row 1, row 2)
        r1 = [0 for _ in range(len(grid[0]))]
        r2 = [0 for _ in range(len(grid[1]))]
        for i in range(len(grid[0])):
            r1[i] = grid[0][i] + r1[i - 1] if (i - 1) >= 0 else grid[0][i]
            r2[i] = grid[1][i] + r2[i - 1] if (i - 1) >= 0 else grid[1][i]
        
        # theory:
        # [2, 7, 11]
        # [1, 6, 7]
        # 
        # when you go down to the bottom, get max value of robot 2 can get
        # by summing all top row entries after current index, and all bottom
        # row entries until the current index
        # e.g.: you go down at index 0. sum all entries in top row after 0 and that's ur answer.
        # e.g. pt 2: compare that against everything before index 0 in bottom row, which is 0
        optimizedRobot2Score = float('inf')
        for i in range(len(grid[0])):
            topSum = r1[-1] - r1[i]
            botSum = r2[i-1] if (i - 1) >= 0 else 0
            maxSum = max(topSum, botSum) # max score robot2 can get in this iteration

            optimizedRobot2Score = min(maxSum, optimizedRobot2Score) # we want robot1 to perform optimally

        return optimizedRobot2Score