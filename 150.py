class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rpnStack = []
        operations = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if (tokens[i] in operations):
                v1 = rpnStack.pop()
                v2 = rpnStack.pop()
                if (tokens[i] == "+"):
                    rpnStack.append(v2 + v1)
                elif (tokens[i] == "-"):
                    rpnStack.append(v2 - v1)
                elif (tokens[i] == "/"):
                    rpnStack.append(int(v2 / v1))
                elif (tokens[i] == "*"):
                    rpnStack.append(v2 * v1)
            else:
                rpnStack.append(int(tokens[i]))

        return rpnStack[0]