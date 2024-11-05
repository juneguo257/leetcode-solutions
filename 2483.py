class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # total penalty if shop closes at ith hour
        penaltyClosePrefix = [0 for _ in range(len(customers))]

        # total penalty if shop stays open till ith hour
        penaltyOpenPrefix = [0 for _ in range(len(customers))]

        for i in range(len(customers)-1, -1, -1):
            if (i == len(customers) - 1):
                if (customers[i] == "Y"):
                    penaltyClosePrefix[i] = 1
            else:
                if (customers[i] == "Y"):
                    penaltyClosePrefix[i] = 1 + penaltyClosePrefix[i+1]
                else:
                    penaltyClosePrefix[i] = penaltyClosePrefix[i+1]
        
        for i in range(len(customers)):
            if (i == 0):
                if (customers[i] == "N"):
                    penaltyOpenPrefix[i] = 1
            else:
                if (customers[i] == "N"):
                    penaltyOpenPrefix[i] = 1 + penaltyOpenPrefix[i-1]
                else:
                    penaltyOpenPrefix[i] = penaltyOpenPrefix[i-1]

        # add together and see
        minInd = 0
        for i in range(1, len(customers) + 1):
            if (minInd == 0):
                minSum = penaltyClosePrefix[0]
            else: # minInd > 0
                minSum = penaltyOpenPrefix[minInd - 1] + penaltyClosePrefix[minInd]
            
            if (i == len(customers)):
                curMinPenalty = penaltyOpenPrefix[-1]
            else: # i < len(customers)
                curMinPenalty = penaltyOpenPrefix[i-1] + penaltyClosePrefix[i]

            if (curMinPenalty < minSum):
                minInd = i
        
        return minInd