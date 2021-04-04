class Solution:
    def mySqrt(self, x: int) -> int:
        eps = 1e-3
        y = 1.0

        while abs(y ** 2 - x) > eps:
            y = (y + x / y) / 2

        return int(y)
