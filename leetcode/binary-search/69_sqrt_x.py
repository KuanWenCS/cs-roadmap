# You are given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Constraints:

# 0 <= x <= ((2^31)-1)


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l + r + 1) // 2
            if mid * mid <= x:
                l = mid
            else:
                r = mid - 1
        return l

        # using lower-bound sol
        # l, r = 0, x
        # while l < r:
        #     mid = (l + r) // 2
        #     if mid * mid >= x:
        #         r = mid
        #     else:
        #         l = mid + 1
        # if l * l > x:
        #     return l - 1
        # return l

        # BF sol.
        # n = 0
        # while (n + 1) * (n + 1) <= x:
        #     if n * n == x:
        #         return n
        #     n += 1
        # return n


if __name__ == "__main__":
    sol = Solution()

    print(sol.mySqrt(0), "\n")
    print(sol.mySqrt(1), "\n")
    print(sol.mySqrt(2), "\n")
    print(sol.mySqrt(9), "\n")
    print(sol.mySqrt(13), "\n")
