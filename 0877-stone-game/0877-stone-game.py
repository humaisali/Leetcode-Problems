class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                takeLeft = piles[left] - dp[left + 1][right]
                takeRight = piles[right] - dp[left][right - 1]

                dp[left][right] = max(takeLeft, takeRight)

        return dp[0][n - 1] > 0