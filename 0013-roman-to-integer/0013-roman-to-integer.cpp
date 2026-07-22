class Solution {
public:
    int romanToInt(string s) {
        int value[128] = {};

        value['I'] = 1;
        value['V'] = 5;
        value['X'] = 10;
        value['L'] = 50;
        value['C'] = 100;
        value['D'] = 500;
        value['M'] = 1000;

        int ans = 0;
        int prev = 0;

        for (int i = s.size() - 1; i >= 0; --i) {
            int curr = value[s[i]];

            if (curr < prev)
                ans -= curr;
            else {
                ans += curr;
                prev = curr;
            }
        }

        return ans;
    }
};