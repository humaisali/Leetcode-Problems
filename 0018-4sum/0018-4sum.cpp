class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        int n = nums.size();

        sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            // Minimum possible sum with current i
            long long minSum = (long long)nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3];
            if (minSum > target)
                break;

            // Maximum possible sum with current i
            long long maxSum = (long long)nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3];
            if (maxSum < target)
                continue;

            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;

                // Minimum possible sum with current i and j
                long long minPair = (long long)nums[i] + nums[j] + nums[j + 1] + nums[j + 2];
                if (minPair > target)
                    break;

                // Maximum possible sum with current i and j
                long long maxPair = (long long)nums[i] + nums[j] + nums[n - 1] + nums[n - 2];
                if (maxPair < target)
                    continue;

                int left = j + 1;
                int right = n - 1;

                while (left < right) {
                    long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        ans.push_back({nums[i], nums[j], nums[left], nums[right]});

                        left++;
                        right--;

                        while (left < right && nums[left] == nums[left - 1])
                            left++;

                        while (left < right && nums[right] == nums[right + 1])
                            right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return ans;
    }
};