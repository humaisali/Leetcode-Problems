class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # memo[(i, M)] = maximum stones current player can get
        memo = {}

        def dfs(i, M):
            # No piles left
            if i >= n:
                return 0

            # We can take all remaining piles
            if 2 * M >= n - i:
                return suffix[i]

            # Already solved
            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                opponent = dfs(i + X, max(M, X))

                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best

            return best

        return dfs(0, 1)