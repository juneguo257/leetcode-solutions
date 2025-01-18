class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        original = [0]
        # either original[0] is 1, or 0, and we can construct list easily from there if possible
        # derived[i] = original[i] ^ original[i+1]
        # derived[i] ^ original[i] = original[i+1]
        for i in range(1, n):
            original.append(derived[i - 1] ^ original[i - 1])
        
        # check if the last condition is satisfied
        # derived[n - 1] = original[n - 1] ^ original[0]
        if (derived[n - 1] == original[n-1] ^ original[0]):
            return True
        
        # either original[0] is must be 1 if possible now
        original = [1]
        for i in range(1, n):
            original.append(derived[i - 1] ^ original[i - 1])
            
        if (derived[n - 1] == original[n-1] ^ original[0]):
            return True

        return False