class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0

        # Calculate XOR of all elements
        for num in nums:
            total_xor ^= num

        # Case 1: Entire array has non-zero XOR
        if total_xor != 0:
            return len(nums)

        # Case 2: Total XOR is zero, but a non-zero element exists
        if any(num != 0 for num in nums):
            return len(nums) - 1

        # Case 3: All elements are zero
        return 0