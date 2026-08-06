# Find First And Last Position of Element In Sorted Array

# You are given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Constraints:

# 0 <= nums.length <= 100,000
# -1,000,000,000 <= nums[i], target <= 1,000,000,000
# nums is a non-decreasing array.

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.findLeft(nums, target)

        # ensure l is valid as well as r, cause l is valid means target in nums
        if (l >= len(nums)) or (nums[l] != target):
            return [-1, -1]

        return [l, self.findRight(nums, target)]

    def findLeft(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        return l

    def findRight(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        return l


if __name__ == "__main__":
    sol = Solution()

    print(sol.searchRange([0], 10), "\n")
