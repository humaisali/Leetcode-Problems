class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # right[j] = the index in word1 where word2[j]
        # can be matched in the right-to-left greedy matching.
        right = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                right[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        used = False

        for i in range(n):

            if j == m:
                break

            # -------------------------------------------------
            # Characters match.
            # Always prefer this earliest index.
            # -------------------------------------------------
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # -------------------------------------------------
            # Characters don't match.
            # We may use this as our one mismatch.
            # -------------------------------------------------
            elif not used:

                # If this is the final character, we can
                # always spend our mismatch here.
                if j == m - 1:
                    ans.append(i)
                    j += 1
                    used = True

                # Otherwise, check whether the rest of word2
                # can be matched after the current index.
                elif right[j + 1] > i:
                    ans.append(i)
                    j += 1
                    used = True

        # We need exactly m selected indices.
        if len(ans) == m:
            return ans

        return []