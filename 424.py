class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounts = {}
        p1 = 0

        maxRepeated = 0 # check neetcode video for reexplanation on why
        longestRCR = 0
        for p2 in range(len(s)):
            if (s[p2] not in charCounts):
                charCounts[s[p2]] = 1
            else:
                charCounts[s[p2]] += 1

            contestCounter = charCounts[s[p2]] # new contestant for most repeated
            maxRepeated = max(maxRepeated, charCounts[s[p2]]) # tricky on why we can do this

            while (k < ((p2 - p1) + 1) - maxRepeated):
                charCounts[s[p1]] -= 1
                p1 += 1
            
            longestRCR = max(longestRCR, ((p2 - p1) + 1))
            
        return longestRCR