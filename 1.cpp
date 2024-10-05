#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <string>

using namespace std;

int solution(vector<int> numbers) {
    unordered_map<int, vector<string>> numbersStr;
    for (int i = 0; i < numbers.size(); ++i) {
        string strNum = to_string(numbers[i]);
        numbersStr[strNum.length()].push_back(strNum);
    }
    
    int count = 0;
    for (const auto& [numsLength, nums] : numbersStr) {
        unordered_map<string, int> seen;
        unordered_set<string> countedPairs;
        for (const string& num : nums) {
            for (int i = 0; i < numsLength; ++i) {
                string masked = num;
                masked[i] = '*';
                if (seen.find(masked) != seen.end()) {
                    string pair = num + "-" + masked;
                    if (countedPairs.find(pair) == countedPairs.end()) {
                        count += seen[masked];
                        countedPairs.insert(pair);
                    }
                }
                seen[masked]++;
            }
        }
    }
    return count;
}