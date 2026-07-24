class Solution {
public:
    vector<string> ans;

    const vector<string> phone = {
        "", "", "abc", "def",
        "ghi", "jkl", "mno",
        "pqrs", "tuv", "wxyz"
    };

    void dfs(const string& digits, int index, string& current) {
        if (index == digits.size()) {
            ans.push_back(current);
            return;
        }

        for (char ch : phone[digits[index] - '0']) {
            current.push_back(ch);
            dfs(digits, index + 1, current);
            current.pop_back();          // Backtrack
        }
    }

    vector<string> letterCombinations(string digits) {
        if (digits.empty())
            return {};

        string current;
        dfs(digits, 0, current);

        return ans;
    }
};