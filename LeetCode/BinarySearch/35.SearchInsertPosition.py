# Search Insert Position

# You are given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Constraints:

# 1 <= nums.length <= 10,000.
# -10,000 < nums[i], target < 10,000
# nums contains distinct values sorted in ascending order.

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        return l


if __name__ == "__main__":
    sol = Solution()

    print(sol.searchInsert([-2, 0, 2, 4, 6, 8], -1), "\n")
