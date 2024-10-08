class Solution:
    def isPalindrome(self, s: str) -> bool:
        ret = "".join(s.lower().split())
        p1 = 0
        p2 = len(ret)-1
        while (p1 < p2):
            if (ret[p1] == ret[p2]):
                p1 += 1
                p2 -= 1
            elif (ord(ret[p1]) >= 48 and ord(ret[p1]) <= 57):
                if (ord(ret[p2]) >= 48 and ord(ret[p2]) <= 57):
                    return False
                elif (ord(ret[p2]) >= 65 and ord(ret[p2]) <= 90):
                    return False
                elif (ord(ret[p2]) >= 97 and ord(ret[p2]) <= 122):
                    return False
                else:
                    p2 -= 1
            elif (ord(ret[p1]) >= 65 and ord(ret[p1]) <= 90):
                if (ord(ret[p2]) >= 65 and ord(ret[p2]) <= 90):
                    return False
                elif (ord(ret[p2]) >= 48 and ord(ret[p2]) <= 57):
                    return False
                elif (ord(ret[p2]) >= 97 and ord(ret[p2]) <= 122):
                    return False
                else:
                    p2 -= 1
            elif (ord(ret[p1]) >= 97 and ord(ret[p1]) <= 122):
                if (ord(ret[p2]) >= 97 and ord(ret[p2]) <= 122):
                    return False
                elif (ord(ret[p2]) >= 65 and ord(ret[p2]) <= 90):
                    return False
                elif (ord(ret[p2]) >= 48 and ord(ret[p2]) <= 57):
                    return False
                else:
                    p2 -= 1
            else:
                p1 += 1
        return True
