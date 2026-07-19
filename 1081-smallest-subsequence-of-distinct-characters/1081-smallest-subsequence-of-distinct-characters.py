class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Step 1: Record the last occurrence of each character
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        visited = set()

        # Step 2: Build the smallest subsequence
        for i, ch in enumerate(s):
            # Skip if already included
            if ch in visited:
                continue

            # Remove larger characters that appear again later
            while (
                stack
                and ch < stack[-1]
                and last[stack[-1]] > i
            ):
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)