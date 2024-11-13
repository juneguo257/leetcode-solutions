class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = -1 # account for null
        lettersSet = set()

        maxLen = 0
        while (p1 < len(s)):
            # if p2 gets behind p1, lettersSet must be empty, so push it back up
            if (p2 < p1):
                p2 += 1
                lettersSet.add(s[p2])
                continue
            
            maxLen = max(maxLen, (p2-p1 + 1))

            if (p2 == len(s) - 1):
                return maxLen
            elif (s[p2 + 1] in lettersSet): # push p1 forward until no dupes
                lettersSet.remove(s[p1])
                p1 += 1
            else:
                p2 += 1
                lettersSet.add(s[p2])

        return maxLen