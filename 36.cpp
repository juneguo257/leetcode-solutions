class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<bool> exists = vector<bool>(10); // numbers 1-9 can fit!
        
        // rows = 9
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                if (board[i][j] != '.') {
                    if (exists[board[i][j] - '0']) {
                        return false;
                    }
                    exists[board[i][j] - '0'] = true;
                }
            }
            exists.clear();
            exists.resize(10, false);
        }

        // columns
        for (int j=0; j<9; j++) {
            for (int i=0; i<9; i++) {
                if (board[i][j] != '.') {
                    if (exists[board[i][j] - '0']) {
                        return false;
                    }
                    exists[board[i][j] - '0'] = true;
                }
            }
            exists.clear();
            exists.resize(10, false);
        }

        // squares
        for(int x = 0; x < 3; x++) { // which square # x-pos
            for (int y = 0; y < 3; y++) { // which square # y-pos
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        char curTile = board[i+(x * 3)][j + (y * 3)];
                        if (curTile != '.') {
                            if (exists[curTile - '0']) {
                                return false;
                            }
                            exists[curTile - '0'] = true;
                        }
                    }
                }
                exists.clear();
                exists.resize(10, false);
            }
        }
        return true;
    }
};