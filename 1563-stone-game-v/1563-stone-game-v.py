class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # --------------------------------------------------
        # Prefix Sum
        # --------------------------------------------------
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # --------------------------------------------------
        # dp[l][r]
        # Maximum score Alice can obtain from l ... r
        # --------------------------------------------------
        dp = [[0] * n for _ in range(n)]

        # --------------------------------------------------
        # left_best[l][r]
        #
        # max of:
        # dp[l][k] + sum(l ... k)
        #
        # for k in [l ... r]
        # --------------------------------------------------
        left_best = [[0] * n for _ in range(n)]

        # --------------------------------------------------
        # right_best[l][r]
        #
        # max of:
        # dp[k][r] + sum(k ... r)
        #
        # for k in [l ... r]
        # --------------------------------------------------
        right_best = [[0] * n for _ in range(n)]

        # Base cases
        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        # --------------------------------------------------
        # Process intervals by increasing length
        # --------------------------------------------------
        for length in range(2, n + 1):

            for l in range(n - length + 1):

                r = l + length - 1

                total = prefix[r + 1] - prefix[l]

                # --------------------------------------------------
                # Find the first split where:
                #
                # left_sum >= right_sum
                #
                # Since all values are positive, left_sum
                # monotonically increases.
                # --------------------------------------------------
                lo = l
                hi = r

                while lo < hi:
                    mid = (lo + hi) // 2

                    left_sum = prefix[mid + 1] - prefix[l]

                    if 2 * left_sum < total:
                        lo = mid + 1
                    else:
                        hi = mid

                k = lo

                best = 0

                # --------------------------------------------------
                # CASE 1:
                #
                # left_sum < right_sum
                #
                # All splits before k belong here.
                #
                # Instead of checking every split:
                #
                # max(
                #     left_sum + dp[l][split]
                # )
                #
                # is already stored in left_best.
                # --------------------------------------------------
                if k > l:
                    best = max(
                        best,
                        left_best[l][k - 1]
                    )

                # --------------------------------------------------
                # k is an actual split if k < r
                # --------------------------------------------------
                if k < r:

                    left_sum = prefix[k + 1] - prefix[l]
                    right_sum = total - left_sum

                    # --------------------------------------------------
                    # CASE 2:
                    # Equal sums
                    # --------------------------------------------------
                    if left_sum == right_sum:

                        best = max(
                            best,
                            left_sum + max(
                                dp[l][k],
                                dp[k + 1][r]
                            )
                        )

                        # Splits after k have:
                        # left_sum > right_sum
                        if k + 1 < r:
                            best = max(
                                best,
                                right_best[k + 2][r]
                            )

                    # --------------------------------------------------
                    # CASE 3:
                    # left_sum > right_sum
                    #
                    # All remaining splits belong here.
                    # --------------------------------------------------
                    else:

                        best = max(
                            best,
                            right_best[k + 1][r]
                        )

                # Store answer for this interval
                dp[l][r] = best

                # --------------------------------------------------
                # Update left_best
                #
                # dp[l][r] + sum(l ... r)
                # --------------------------------------------------
                left_best[l][r] = max(
                    left_best[l][r - 1],
                    dp[l][r] + total
                )

                # --------------------------------------------------
                # Update right_best
                #
                # dp[l][r] + sum(l ... r)
                # --------------------------------------------------
                right_best[l][r] = max(
                    right_best[l + 1][r],
                    dp[l][r] + total
                )

        return dp[0][n - 1]