class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int p1 = 0;
        int p2 = numbers.size() - 1;
        vector<int> ret;
        while (p1 < p2) {
            if (numbers[p1] + numbers[p2] == target) {
                ret.push_back(p1 + 1);
                ret.push_back(p2 + 1);
                return ret;
            } else if (numbers[p1] + numbers[p2] > target) {
                p2--;
            } else if (numbers[p1] + numbers[p2] < target) {
                p1++;
            }
        }
        return ret;
    }
};