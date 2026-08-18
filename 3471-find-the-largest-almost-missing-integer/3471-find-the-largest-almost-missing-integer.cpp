class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        int n = nums.size();

        // Case 1: k == 1
        if (k == 1) {
            unordered_map<int, int> freq;

            for (int x : nums) {
                freq[x]++;
            }

            int ans = -1;

            for (auto& [x, count] : freq) {
                if (count == 1) {
                    ans = max(ans, x);
                }
            }

            return ans;
        }

        // Case 2: k == n
        if (k == n) {
            return *max_element(nums.begin(), nums.end());
        }

        // Case 3: 1 < k < n
        int ans = -1;

        // Check first element
        int first = nums[0];
        bool uniqueFirst = true;

        for (int i = 1; i < n; i++) {
            if (nums[i] == first) {
                uniqueFirst = false;
                break;
            }
        }

        if (uniqueFirst) {
            ans = max(ans, first);
        }

        // Check last element
        int last = nums[n - 1];
        bool uniqueLast = true;

        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == last) {
                uniqueLast = false;
                break;
            }
        }

        if (uniqueLast) {
            ans = max(ans, last);
        }

        return ans;
    }
};