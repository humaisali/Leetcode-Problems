class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxArea = 0;

        while (left < right) {
            int width = right - left;
            int currentHeight = min(height[left], height[right]);
            maxArea = max(maxArea, width * currentHeight);

            // Move the pointer with the smaller height
            if (height[left] < height[right])
                left++;
            else
                right--;
        }

        return maxArea;
    }
};