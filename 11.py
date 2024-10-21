class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        maxHeight = 0

        while (p1 < p2):
            curHeight = (p2-p1) * (min(height[p1], height[p2]))
            maxHeight = max(maxHeight, curHeight)

            if (height[p1] < height[p2]):
                p1 += 1
            else:
                p2 -= 1

        return maxHeight