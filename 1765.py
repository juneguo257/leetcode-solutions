from collections import deque

class Solution:
    def handleTile(self, node, q, m, n, retMap):
        i, j, newDepth = node
        if (i >= 0 and i < m):
            if (j >= 0 and j < n):
                if (retMap[i][j] == -1):
                    retMap[i][j] = newDepth
                    self.addNeighborsToQueue(q, i, j, newDepth + 1)

    def addNeighborsToQueue(self, q, i, j, newDepth):
        q.append((i + 1, j, newDepth))
        q.append((i - 1, j, newDepth))
        q.append((i, j - 1, newDepth))
        q.append((i, j + 1, newDepth))

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        # init the map w/ -1 (denotes height hasn't been init'd yet)
        retMap = [[-1 for _ in range(n)] for _ in range(m)]
        q = deque()

        # fill in water first
        for i in range(m):
            for j in range(n):
                if (isWater[i][j] == 1):
                    retMap[i][j] = 0

        # then get the layers around the water
        for i in range(m):
            for j in range(n):
                if (retMap[i][j] == 0):
                    # fill in land around water
                    if (i - 1 >= 0 and retMap[i - 1][j] == -1): # up
                        retMap[i - 1][j] = 1
                        self.addNeighborsToQueue(q, i - 1, j, 2)
                    if (i + 1 < m and retMap[i + 1][j] == -1): # down
                        retMap[i + 1][j] = 1
                        self.addNeighborsToQueue(q, i + 1, j, 2)
                    if (j - 1 >= 0 and retMap[i][j - 1] == -1): # left
                        retMap[i][j - 1] = 1
                        self.addNeighborsToQueue(q, i, j - 1, 2)
                    if (j + 1 < n and retMap[i][j + 1] == -1): # right
                        retMap[i][j + 1] = 1
                        self.addNeighborsToQueue(q, i, j + 1, 2)
        
        while (len(q) > 0):
            self.handleTile(q.popleft(), q, m, n, retMap)
        
        return retMap