class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Count stones according to their remainder when divided by 3
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        # If the number of remainder-0 stones is even,
        # Alice wins if both remainder-1 and remainder-2 stones exist.
        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > 0

        # If the number of remainder-0 stones is odd,
        # Alice wins only if the difference between
        # remainder-1 and remainder-2 stones is greater than 2.
        return abs(count[1] - count[2]) > 2