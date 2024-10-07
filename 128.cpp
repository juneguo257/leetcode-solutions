class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> setNums;
        for (int num : nums) {
            setNums.insert(num);
        }

        int maxRet = 0;

        for (int i=0; i<nums.size(); i++) {
            if (!setNums.contains(nums[i] - 1)) {
                int cur = nums[i];
                int curCount = 0;
                while (setNums.contains(cur)) {
                    cur++;
                    curCount++;
                }
                maxRet = std::max(maxRet, curCount);
            }
        }
        return maxRet;
    }
};