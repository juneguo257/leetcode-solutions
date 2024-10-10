class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        for i in range(len(s)):
            if (s[i] == "("):
                bracketStack.append(")")
            elif (s[i] == "{"):
                bracketStack.append("}")
            elif (s[i] == "["):
                bracketStack.append("]")
            elif (len(bracketStack) == 0):
                return False
            elif (s[i] == ")" and bracketStack[-1] == ")"):
                bracketStack.pop()
            elif (s[i] == "}" and bracketStack[-1] == "}"):
                bracketStack.pop()
            elif (s[i] == "]" and bracketStack[-1] == "]"):
                bracketStack.pop()
            else:
                return False
        return len(bracketStack) == 0