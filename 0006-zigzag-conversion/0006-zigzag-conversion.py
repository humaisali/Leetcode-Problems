class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list for each row
        rows = [""] * numRows

        currentRow = 0
        goingDown = False

        for ch in s:
            rows[currentRow] += ch

            # Change direction at the first or last row
            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown

            currentRow += 1 if goingDown else -1

        return "".join(rows)