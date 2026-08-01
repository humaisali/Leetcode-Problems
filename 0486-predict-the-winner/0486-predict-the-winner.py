from functools import cache
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dp(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            return max(
                nums[left] - dp(left + 1, right),
                nums[right] - dp(left, right - 1)
            )

        return dp(0, len(nums) - 1) >= 0