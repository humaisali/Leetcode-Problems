class Solution:
    def missingInteger(self, nums):
        # Step 1: Find the sum of the longest sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Step 2: Store all numbers for fast lookup
        nums_set = set(nums)

        # Step 3: Find the smallest missing integer >= total
        answer = total

        while answer in nums_set:
            answer += 1

        return answer