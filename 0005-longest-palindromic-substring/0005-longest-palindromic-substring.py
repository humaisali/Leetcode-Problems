class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        maxLength = 1

        def expand(left, right):
            nonlocal start, maxLength

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if right - left + 1 > maxLength:
                    start = left
                    maxLength = right - left + 1

                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)       # Odd length
            expand(i, i + 1)   # Even length

        return s[start:start + maxLength]