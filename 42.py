class Solution:
    def trap(self, height: List[int]) -> int:
        lMax = height[0]
        rMax = height[-1]

        i = 0
        j = len(height) - 1
        updatedI = True
        waterTotal = 0
        while (i < j):
            #print("lMax: " + str(lMax) + ", rMax: " + str(rMax))

            if (updatedI):
                #print("i: " + str(i))
                waterTotal += max(0, min(lMax, rMax) - height[i])
            else:
                #print("j: " + str(j))
                waterTotal += max(0, min(lMax, rMax) - height[j])
            
            if (lMax <= rMax):
                i += 1
                lMax = max(height[i], lMax)
                updatedI = True
            else:
                j -= 1
                rMax = max(height[j], rMax)
                updatedI = False
    
        return waterTotal