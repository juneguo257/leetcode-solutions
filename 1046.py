import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        # turn stones into an inverted min-heap
        heapq.heapify(stones)

        while (len(stones) >= 2):
            y = heapq.heappop(stones)
            y *= -1

            x = heapq.heappop(stones)
            x *= -1

            if (x < y):
                heapq.heappush(stones, (y - x) * -1)
        
        if (len(stones) == 0):
            return 0
        else:
            return (stones[0] * -1)