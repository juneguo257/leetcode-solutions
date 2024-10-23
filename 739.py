class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        soln = [0 for i in range(len(temperatures))]

        # theory: whenever stack gets filled with more numbers, numbers can
        # only go down, so when things get popped, it works out!

        # ***conjecture*** :sparkles: lowest element will always be at top of stack

        tempStack = []
        for i in range(len(temperatures)):
            if (len(tempStack) == 0):
                tempStack.append(i) # store indicies
            elif (temperatures[i] > temperatures[tempStack[-1]]):
                while (len(tempStack) > 0 and temperatures[i] > temperatures[tempStack[-1]]):
                    lastEle = tempStack.pop()
                    soln[lastEle] = i - lastEle
                tempStack.append(i)
            else:
                tempStack.append(i)

        return soln