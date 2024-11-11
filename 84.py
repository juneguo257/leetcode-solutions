class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # NOTE: numbers that non-descending are always beneficial to keep in mind
        heightStack = []

        maxArea = 0
        for i in range(len(heights)):
            if (len(heightStack) == 0):
                heightStack.append((0, heights[i]))
            
            # if >, append to stack no problemo
            if (heights[i] > heightStack[-1][1]):
                heightStack.append((i, heights[i]))
            elif (heights[i] == heightStack[-1][1]): # do nothing cause existing stack entry accounts for it
                continue
            elif (heights[i] < heightStack[-1][1]):
                # iterate through stack until height is matched or lower
                lastInd = i
                while (len(heightStack) > 0 and heightStack[-1][1] > heights[i]):
                    lastInd, lastHt = heightStack.pop()
                    maxArea = max(maxArea, (i - lastInd) * (lastHt)) # w * h made by that entry
                
                # create an entry with the current index
                heightStack.append((lastInd, heights[i]))
        
        # now, calculate the rectangles that made it to the end
        while (len(heightStack) > 0):
            lastInd, lastHt = heightStack.pop()
            maxArea = max(maxArea, (len(heights) - lastInd) * (lastHt)) # w * h made by that entry
        
        return maxArea

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         # theory: add numbers to a stack, once it's lower, pop until we reach that number
#         heightStack = []
#         maxArea = 0
#         for i in range(len(heights)):
#             if len(heightStack) == 0:
#                 heightStack.append(heights[i])
#                 continue
            
#             if heights[i] > heightStack[-1]:
#                 heightStack.append(heights[i])
#             elif heights[i] == heightStack[-1]: # it'll be optimal later, but not worth checking now
#                 heightStack.append(heights[i])
#             elif heights[i] < heightStack[-1]:
#                 popCount = 1
#                 minHeight = heightStack.pop()
#                 while (len(heightStack) > 0 and heights[i] < heightStack[-1]):
#                     curEle = heightStack.pop()
#                     if (curEle < minHeight):
#                         maxArea = max(popCount * minHeight, maxArea)
#                         minHeight = curEle

#                     popCount += 1
    
#                 maxArea = max(popCount * minHeight, maxArea)

#                 # add back all the heights that are now effectively lower
#                 while (popCount > 0):
#                     heightStack.append(min(minHeight, heights[i]))
#                     popCount -= 1

#                 heightStack.append(heights[i])
        
#         # heightStack will always have >= 1 element

#         c = 1 # repeated iterations of current element
#         maxHeight = heightStack.pop() # current maximum height of rectangle

#         while (len(heightStack) > 0):
#             curEle = heightStack.pop()
#             if (curEle < maxHeight):
#                 maxArea = max(maxHeight * c, maxArea)
#                 maxHeight = curEle
#             c += 1
        
#         maxArea = max(maxHeight * c, maxArea) # account for last element being the largest
        
#         return maxArea