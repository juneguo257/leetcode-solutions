class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # turn s1 into a dictionary
        s1Dict = {}
        for i in range(len(s1)):
            if (s1[i] in s1Dict):
                s1Dict[s1[i]] += 1
            else:
                s1Dict[s1[i]] = 1
        
        s1Distance = len(s1) # distance away from s1 (sum of s1Dict)

        # GAMEPLAN: subtract from s1Dict
        p1 = 0
        for p2 in range(len(s2)):
            if (p2 < p1):
                continue
            
            if (s1Distance == 0):
                return True
            elif (s2[p2] in s1Dict):
                if (s1Dict[s2[p2]] > 0):
                    s1Dict[s2[p2]] -= 1
                    s1Distance -= 1
                else:
                    s1Dict[s2[p2]] -= 1
                    s1Distance -= 1
                    while (s1Dict[s2[p2]] < 0): # when 0, back to good
                        s1Dict[s2[p1]] += 1
                        s1Distance += 1
                        p1 += 1
            else:
                while (p1 < p2):
                    s1Dict[s2[p1]] += 1
                    s1Distance += 1
                    p1 += 1
                
                p1 += 1 # avoid including current unused letter
        
        return (s1Distance == 0)