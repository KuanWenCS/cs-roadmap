# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in O(logn) time.

# Constraints:

# 1 <= nums.length <= 10000.
# -10000 < nums[i], target < 10000
# All the integers in nums are unique.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

        # BP, lower_bound is not a built-in func.
        # idx = lower_bound(nums, target)

        # if idx == len(nums):
        #     return -1

        # if nums[idx] != target:
        #     return -1

        # return idx

        # not BP
        # l, r = 0, len(nums)
        # while r - l > 1:
        #     mid = (l + r) // 2
        #     if target == nums[mid]:
        #         return mid
        #     elif target < nums[mid]:
        #         r = mid
        #     else:
        #         l = mid
        # if target == nums[l]:
        #     return l
        # return -1


if __name__ == "__main__":
    sol = Solution()

    print(sol.search([0], 1), "\n")
