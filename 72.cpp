#include <iostream>

using namespace std;

int sim(int (*dp)[25], string &word1, string &word2, int p1, int p2, int ops)
{
    if (p1 >= word1.length() && p2 >= word2.length())
    {
        dp[p1][p2] = ops;
    }
    else if (p1 >= word1.length())
    {
        dp[p1][p2] = sim(dp, word1, word2, p1, p2 + 1, ops + 1); // add to word1
    }
    else if (p2 >= word2.length())
    {
        dp[p1][p2] = sim(dp, word1, word2, p1 + 1, p2, ops + 1); // remove from word1
    }
    else if (word1[p1] == word2[p2])
    {
        dp[p1][p2] = sim(dp, word1, word2, p1 + 1, p2 + 1, ops); // match!
    }
    else
    {
        int addW1 = sim(dp, word1, word2, p1, p2 + 1, ops + 1);         // add to word1
        int removeW1 = sim(dp, word1, word2, p1 + 1, p2, ops + 1);      // remove from word1
        int replaceW1 = sim(dp, word1, word2, p1 + 1, p2 + 1, ops + 1); // replace in word1
        dp[p1][p2] = std::min(addW1, std::min(removeW1, replaceW1));
    }
    return dp[p1][p2];
}

int minDistance(string word1, string word2)
{
    int dp[25][25];
    return sim(dp, word1, word2, 0, 0, 0);
}

int main()
{
    cout << minDistance("abc", "abd") << endl;
    return 0;
}
