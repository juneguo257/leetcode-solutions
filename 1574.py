class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # equivalent problem: longest non-decreasing array after removing subarray

        # possibilites: remove subarray in beginning, middle, or end
        longestArrayPossible = 1
        
        # beginning: just look for nondecreasing subarray at the end
        prev = arr[-1]
        
        # define ptrs for middle two-ptr solution
        p1 = 0
        p2 = len(arr) - 1

        # beginning soln loop
        for i in range(len(arr) - 2, -1, -1):
            if (arr[i] <= prev):
                prev = arr[i]
                p2 = i
                longestArrayPossible = max(longestArrayPossible, len(arr) - i)
            else:
                break
        
        # middle: two pointer soln (phase 1: shifting 2nd ptr) [done above]

        # phase two of two pointer (shifting 1st ptr)
        prev = arr[0]
        while (p1 < p2 and arr[p1] >= prev):
            prev = arr[p1]
            longestArrayPossible = max(longestArrayPossible, (len(arr) - p2) + (p1))

            while (p2 < len(arr) and arr[p2] < arr[p1]):
                p2 += 1

            p1 += 1

        # one last case cause everything before p1 counts
        longestArrayPossible = max(longestArrayPossible, (len(arr) - p2) + (p1))
        
        # end: just look for nondecreasing subarrays at the beginning (done above in phase 2)
                
        return len(arr) - longestArrayPossible