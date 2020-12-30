/**
79. Word Search
https://leetcode.com/problems/word-search/
*/

class Solution
{

    vector<vector<char>> board;

    string word;

public:
    bool exist(vector<vector<char>> &board, string word)
    {

        this->board = board;
        this->word = word;

        for (int i = 0; i < board.size(); i++)
            for (int j = 0; j < board[i].size(); j++)
            {
                if (backtrack(i, j, 0))
                    return true;
            }

        return false;
    }

    bool backtrack(int i, int j, int x)
    {
        if (x == word.length())
            return true;

        if (i < 0 || i >= board.size() || j < 0 || j >= board[i].size() || board[i][j] < 65)
        {
            return false;
        }

        if (board[i][j] == word[x])
        {
            board[i][j] -= 65;

            if (backtrack(i + 1, j, x + 1) ||
                backtrack(i, j + 1, x + 1) ||
                backtrack(i - 1, j, x + 1) ||
                backtrack(i, j - 1, x + 1))

                return true;
            board[i][j] += 65;
        }

        return false;
    }

    void print_board()
    {
        for (int i = 0; i < board.size(); i++)
            for (int j = 0; j < board[i].size(); j++)
                cout << board[i][j];
    }
};