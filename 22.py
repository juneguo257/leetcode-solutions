class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pStack = []
        ans = []

        if (n > 0):
            pStack.append(("(", 1, n - 1, n)) # number represents # of ( left to end
        else:
            return []

        while (len(pStack) > 0):
            curEle = pStack.pop()
            beginP = curEle[2]
            endP = curEle[3]
            if (beginP == 0 and endP == 0):
                ans.append(curEle[0])
            else:
                if (beginP > 0):
                    pStack.append((curEle[0] + "(", curEle[1] + 1, beginP - 1, endP))
                
                if (endP > 0 and curEle[1] > 0):
                    pStack.append((curEle[0] + ")", curEle[1] - 1, beginP, endP - 1))
        return ans