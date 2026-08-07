# Search a 2D Matrix

# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10000 <= matrix[i][j], target <= 10000

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findCol(matrix, target)
        return self.findTarget(matrix[row], target)

    def findCol(self, matrix: List[List[int]], target: int) -> int:
        l, r = 0, len(matrix) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if matrix[mid][0] <= target:
                l = mid
            else:
                r = mid - 1
        return l

    def findTarget(self, row: List[int], target: int) -> bool:
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


if __name__ == "__main__":
    sol = Solution()

    # print(
    #     "\noutput: ",
    #     sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10),
    #     "\n",
    # )
    # print(
    #     "\noutput: ",
    #     sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
    #     "\n",
    # )
    # print(
    #     "\noutput: ",
    #     sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15),
    #     "\n",
    # )
    print(
        "\noutput: ",
        sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
        "\n",
    )
    # print("\noutput: ", sol.searchMatrix([[]], 8), "\n")
