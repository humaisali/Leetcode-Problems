class Solution {
public:
    vector<string> result;

    void backtrack(string& current, int open, int close, int n) {
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }

        if (open < n) {
            current.push_back('(');
            backtrack(current, open + 1, close, n);
            current.pop_back();   // Backtrack
        }

        if (close < open) {
            current.push_back(')');
            backtrack(current, open, close + 1, n);
            current.pop_back();   // Backtrack
        }
    }

    vector<string> generateParenthesis(int n) {
        string current;
        backtrack(current, 0, 0, n);
        return result;
    }
};